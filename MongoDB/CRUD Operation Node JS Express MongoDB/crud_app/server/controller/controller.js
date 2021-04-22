var Employeedb = require('../model/model');

// create and save new user
exports.create = (req,res)=>{
    // validate request
    if(!req.body){
        res.status(400).send({message: "Content can not be empty!"});
        return;
    }

    // new user
    const user = new Employeedb({
        name: req.body.name,
        email: req.body.email,
        gender: req.body.gender,
        status: req.body.status
    })

    // save user in the database
    user
        .save(user)
        .then(data=>{
            // res.send(data)
            res.redirect('/add-user')
        })
        .catch(err=>{
            res.status(500).send({
                message: err.message || "Some error occured while creating a create operation"
            });
        });
}

// retrieve and return all users/ retrive and return a single user
exports.find = (req, res)=>{

    if(req.query.id){
        const id = req.query.id;

        Employeedb.findById(id)
            .then(data=>{
                if(!data){
                    res.status(404).send({message: "Not Found user with id" + id})
                }else{
                    res.send(data)
                }
            })
            .catch(err=>{
                res.status(500).send({message: "Error retrieving user with given id" + id})
            })
    }else{
        Employeedb.find()
            .then(user=>{
                res.send(user)
            })
            .catch(err=>{
                res.status(500).send({message: err.message || "Error Occurred while retreiving employee information"})
            })
    }

}

// Update a new idetified user by user id
exports.update = (req, res)=>{
    if(!req.body){
        return res
            .status(400)
            .send({message: "Data to update can not be empty"})
    }

    const id = req.params.id;
    Employeedb.findByIdAndUpdate(id, req.body, {useFindAndModify: false})
        .then(data=>{
            if(!data){
                res.status(404).send({message: `Cannot Update user with ${id}. Maybe user not found!`})
            }else{
                res.send(data)
            }
        })
        .catch(err=>{
            res.status(500).send({message: "Error Update user information!"})
        })
}

// Delete a user with specified user id in the request
exports.delete = (req, res)=>{
    const id = req.params.id;

    Employeedb.findByIdAndDelete(id)
        .then(data=>{
            if(!data){
                res.status(404).send({message:`Cannot delete with id $(id). Entered id is incorrect`})
            }else{
                res.send({
                    message:"User deleted successfully!"
                })
            }
        })
        .catch(err=>{
            res.status(500).send({
                message: "Could not delete User with id=" + id
            });
        });
}