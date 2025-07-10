
<template>
  <div class="support-page">
    <h1>Support Chat</h1>
    <p>Welcome to ixome.ai Support! Let’s get your tech sorted with a friendly chat!</p>
    <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
    <div v-if="loading" class="loading">Connecting to our team...</div>
    <div v-if="messages.length" class="chat-messages">
      <div v-for="message in messages" :key="message.id" :class="['message', message.sender === currentUserId ? 'sent' : 'received']">
        <div class="message-content">
          <strong>{{ message.sender }}</strong>
          <p>{{ message.text }}</p>
          <span class="timestamp">{{ formatTimestamp(message.timestamp) }}</span>
        </div>
      </div>
    </div>
    <div v-else class="no-messages">Hey there! Start chatting with us to get help!</div>
    <div class="chat-input">
      <input v-model="newMessage" placeholder="Type your message here..." @keyup.enter="sendMessage" :disabled="loading" />
      <button @click="sendMessage" :disabled="loading">Send</button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, onUnmounted } from "vue";
import io from "socket.io-client";

export default defineComponent({
  name: "Support",
  setup() {
    const socket = ref(null);
    const currentUserId = ref(localStorage.getItem('user_id') || "guest");
    const messages = ref([]);
    const newMessage = ref("");
    const errorMessage = ref("");
    const loading = ref(true);
    const firstVisit = ref(!localStorage.getItem('first_visit_done'));

    onMounted(() => {
      try {
        const token = localStorage.getItem('jwt_token');
        if (!token) {
          errorMessage.value = "Oops! Please log in to start chatting.";
          loading.value = false;
          return;
        }

        socket.value = io("http://localhost:5001", {
          query: { token, user_id: currentUserId.value }
        });

        socket.value.on("connect", () => {
          console.log("Connected to Socket.IO server");
          loading.value = false;
          messages.value.push({
            id: Date.now(),
            sender: "System",
            text: "Hey there! I’m your ixome.ai chatbot—ready to help with a smile! 😄",
            timestamp: new Date().getTime(),
          });
          if (firstVisit.value) {
            localStorage.setItem('first_visit_done', 'true');
          }
        });

        socket.value.on("response", (data) => {
          messages.value.push({
            id: Date.now(),
            sender: "Bot",
            text: data.text,
            timestamp: new Date().getTime(),
          });
          if (data.redirect) {
            window.location.href = data.redirect;
          }
        });

        socket.value.on("connect_error", (error) => {
          errorMessage.value = `Whoops! Connection issue: ${error.message}`;
          console.error("Socket.IO connection error:", error);
          loading.value = false;
        });
      } catch (error) {
        errorMessage.value = `Yikes! Chat setup failed: ${error.message}`;
        console.error("Chat initialization error:", error);
        loading.value = false;
      }
    });

    onUnmounted(() => {
      if (socket.value) {
        socket.value.disconnect();
      }
    });

    const sendMessage = () => {
      if (!newMessage.value.trim() || !socket.value) return;
      try {
        socket.value.emit("message", {
          user_id: currentUserId.value,
          text: newMessage.value,
        });
        messages.value.push({
          id: Date.now(),
          sender: currentUserId.value,
          text: newMessage.value,
          timestamp: new Date().getTime(),
        });
        newMessage.value = "";
      } catch (error) {
        errorMessage.value = `Oops! Couldn’t send your message: ${error.message}`;
        console.error("Message sending error:", error);
      }
    };

    const formatTimestamp = (timestamp) => {
      const date = new Date(timestamp);
      return date.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
    };

    return {
      currentUserId,
      messages,
      newMessage,
      errorMessage,
      loading,
      sendMessage,
      formatTimestamp,
    };
  },
});
</script>

<style scoped>
.support-page {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
  margin-top: 60px;
  z-index: 10;
  font-family: Arial, sans-serif;
  background-color: #f7fafd;
}

.support-page h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
  color: #333;
}

.support-page p {
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
  color: #666;
}

.error-message {
  color: #d9534f;
  margin-bottom: 1rem;
  padding: 10px;
  background-color: #fff3f3;
  border-radius: 4px;
}

.loading {
  font-size: 1.2rem;
  color: #007bff;
  margin-bottom: 1rem;
}

.chat-messages {
  max-height: 400px;
  overflow-y: auto;
  border: 1px solid #ddd;
  padding: 10px;
  margin-bottom: 1rem;
  background-color: white;
  border-radius: 4px;
}

.no-messages {
  font-size: 1rem;
  color: #666;
  margin-bottom: 1rem;
  padding: 10px;
  background-color: #f9f9f9;
  border-radius: 4px;
}

.message {
  display: flex;
  align-items: flex-start;
  margin-bottom: 10px;
}

.message.sent {
  justify-content: flex-end;
}

.message.received {
  justify-content: flex-start;
}

.message-content {
  background-color: #f1f1f1;
  padding: 8px 12px;
  border-radius: 8px;
  max-width: 70%;
}

.message.sent .message-content {
  background-color: #007bff;
  color: white;
}

.timestamp {
  font-size: 0.8rem;
  color: #999;
  margin-top: 4px;
  display: block;
}

.chat-input {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}

.chat-input input {
  flex-grow: 1;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

.chat-input input:disabled {
  background-color: #f8f9fa;
  cursor: not-allowed;
}

.chat-input button {
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}

.chat-input button:hover {
  background-color: #0056b3;
}

.chat-input button:disabled {
  background-color: #6c757d;
  cursor: not-allowed;
}

@media (max-width: 768px) {
  .support-page {
    padding: 10px;
    margin-top: 50px;
  }

  .support-page h1 {
    font-size: 1.5rem;
  }

  .support-page p {
    font-size: 1rem;
  }

  .chat-messages {
    max-height: 300px;
  }

  .chat-input input {
    font-size: 0.9rem;
  }

  .chat-input button {
    font-size: 0.9rem;
    padding: 6px 12px;
  }
}
</style>