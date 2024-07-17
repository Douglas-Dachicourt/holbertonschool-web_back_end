import getNeighborhoodsList from './2-arrow.js';

const neighborhoodsList = new getNeighborhoodsList();
const res = neighborhoodsList.addNeighborhood('Noe Valley');
console.log(res);

//   export default function getNeighborhoodsList() {
//     this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];
  
//     const self = this;
//     this.addNeighborhood = function add(newNeighborhood) {
//       self.sanFranciscoNeighborhoods.push(newNeighborhood);
//       return self.sanFranciscoNeighborhoods;
//     };
//   }