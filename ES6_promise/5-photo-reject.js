export default function uploadPhoto(filename) {
  const fileName = filename
  return Promise.reject(
    new Error(`${fileName} cannot be processed`),
  )
}
