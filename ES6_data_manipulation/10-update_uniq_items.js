export default function updateUniqueItems(map) {
  const newMap = map;

  if (newMap instanceof Map === false) {
    throw new Error('Cannot process');
  }

  for (const [key, value] of newMap) {
    if (value === 1) {
      newMap.set(key, 100);
    }
  }
  return newMap;
}
