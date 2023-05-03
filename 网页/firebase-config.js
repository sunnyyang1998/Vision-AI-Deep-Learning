// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBguSCdkwKWLq0uT7hiZpMcfLcS8siXr-Y",
  authDomain: "catering-management-syst-78dec.firebaseapp.com",
  projectId: "catering-management-syst-78dec",
  storageBucket: "catering-management-syst-78dec.appspot.com",
  messagingSenderId: "570867869273",
  appId: "1:570867869273:web:fa8cb0d0de92ed2b8e3348",
  measurementId: "G-XGFT8K55LL"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);


