import { CometChat } from '@cometchat-pro/chat';
import { defineNuxtPlugin } from '#app';

export default defineNuxtPlugin(async () => {
  const UID = 'cometchat-uid-1'; // Test user ID
  const authKey = '607b997630329c92573a973d27230d23e152f3cd'; // Replace with your Auth Key

  try {
    // Check if a user is already logged in
    const user = await CometChat.getLoggedinUser();
    if (!user) {
      // Log in the test user
      const loggedInUser = await CometChat.login(UID, authKey);
      console.log('CometChat user login successful:', loggedInUser);
    } else {
      console.log('CometChat user already logged in:', user);
    }
  } catch (error) {
    console.error('CometChat user login failed:', error);
  }
});
