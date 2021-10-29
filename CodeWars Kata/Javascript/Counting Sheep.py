function countSheeps(arrayOfSheep) {
  var count = 0 ;
  for (var x of arrayOfSheep){
    
    if (x === true){
      count += 1 ;
    } else {
      count += 0
    }
    

  }
    return count
}
