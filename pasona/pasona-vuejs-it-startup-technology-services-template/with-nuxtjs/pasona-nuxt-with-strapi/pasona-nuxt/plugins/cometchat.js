import { CometChat } from '@cometchat-pro/chat';
import { defineNuxtPlugin } from '#app';

export default defineNuxtPlugin(() => {
  const appID = '2758884303d8a311'; // Your App ID
  const region = 'us'; // Your Region
  const appSetting = new CometChat.AppSettingsBuilder()
    .subscribePresenceForAllUsers()
    .setRegion(region)
    .build();

  CometChat.init(appID, appSetting).then(
    () => {
      console.log('CometChat initialized successfully');
    },
    error => {
      console.error('CometChat initialization failed', error);
    }
  );
});
