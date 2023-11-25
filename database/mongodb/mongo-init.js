console.log("GOT TO THE SCRIIIIIIIIIIIIIIIIIIIIIIIPT")


user = db.getSiblingDB("ml_service_db")

user.createUser({
  user: "ml_service_user",
  pwd: "ml_service_password",
  roles: [{ role: "readWrite", db: "ml_service_db" }]
})

let res = [
  user.container.drop(),
  user.container.createIndex({ myfield: 1 }, { unique: true }),
  user.container.insert({ myfield: 'hello', thatfield: 'testing' }),
]



