export default function getResponseFromAPI() {
  const promise = new Promise((resolve, reject) => {
    const success = true;
    if (success) {
      resolve('Success');
    } else {
      reject(new Error('Error'));
    }
  });

  return promise;
}
