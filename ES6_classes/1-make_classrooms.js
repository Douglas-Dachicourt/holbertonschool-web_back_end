import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const array = [];
  const newClass = new ClassRoom(19);
  const newClass2 = new ClassRoom(20);
  const newClass3 = new ClassRoom(34);

  array.push(newClass, newClass2, newClass3);

  return array;
}
