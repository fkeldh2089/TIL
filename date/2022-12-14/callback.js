function findUser(id, cb) {
  let user;
  setTimeout(function () {
    console.log("waited 0.1 sec.");
    user = {
      id: id,
      name: "User" + id,
      email: id + "@test.com",
    };
  }, 100);
  cb(user)
  return user;
}

const user = findUser(1, function(user){
  console.log(user)
});
console.log("user:", user);