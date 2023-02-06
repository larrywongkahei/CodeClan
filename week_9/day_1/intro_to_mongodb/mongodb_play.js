use zoo;

const id = ObjectId('63c55be2acd1aee9444c0192')

db.animals.findOne({_id: id})

db.animals.updateOne(
    {
        _id: ObjectId('63c55be2acd1aee9444c0193')
    },
    {
        $set: {name: "Steve"}
    }
)
db.animals.findOne({_id: ObjectId('63c55be2acd1aee9444c0193')})

db.animals.deleteOne({_id: ObjectId('63c55be2acd1aee9444c0193')})