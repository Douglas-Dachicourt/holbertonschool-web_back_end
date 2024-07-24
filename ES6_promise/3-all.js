import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  Promise.all([uploadPhoto(), createUser()])
    .then(([photo, user]) => {
      if (photo && user) {
        console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
      } else {
        console.log('Invalid data from promises');
      }
    })
    .catch((error) => {
      console.log('Signup system offline');
      console.log(error);
    });
}
