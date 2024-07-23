export default function handleResponseFromAPI(promise) {
  let newPromise = promise;
  newPromise = new Promise((resolve, reject) => {
    const success = true;
    if (success) {
      resolve({
        status: 200,
        body: 'success',
      });
    } else {
      reject(new Error(Error));
    }
  })
    .then(() => console.log('Got a response from the API'));

  return newPromise;
}
