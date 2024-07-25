export default function loadBalancer(chinaDownload, USDownload) {
  const promises = [chinaDownload, USDownload];
  return Promise.any(promises)
    .then((value) => {
      return value;
    })
    .catch((err) => {
      throw err;
    });
}
