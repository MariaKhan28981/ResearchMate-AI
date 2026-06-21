import { useState } from "react"
import client from "../api/client"


function Upload(){

    const [file,setFile] = useState(null)
    const [status,setStatus] = useState("")


    async function upload(){

        if(!file){

            setStatus("Please select a PDF")

            return
        }


        const formData = new FormData()

        formData.append(
            "file",
            file
        )


        try{

            setStatus("Processing paper...")


            const response = await client.post(
                "/upload",
                formData,
                {
                    headers:{
                        "Content-Type":"multipart/form-data"
                    }
                }
            )


            setStatus(
                response.data.message
            )


        }catch(error){

            console.log(error)

            setStatus("Upload failed")

        }

    }



    return (

        <div className="p-6 border rounded-xl">


            <h2 className="text-2xl font-bold mb-4">
                Upload Research Paper
            </h2>



            <label

                htmlFor="paper-upload"

                className="cursor-pointer bg-gray-200 px-4 py-2 rounded"

            >

                Choose PDF

            </label>



            <input

                id="paper-upload"

                type="file"

                accept=".pdf"

                className="hidden"

                onChange={
                    e=>{

                        setFile(e.target.files[0])

                        setStatus(
                            e.target.files[0]?.name
                        )

                    }
                }

            />



            <button

                type="button"

                onClick={upload}

                className="ml-3 bg-black text-white px-5 py-2 rounded"

            >

                Upload

            </button>



            <p className="mt-4">

                {status}

            </p>


        </div>

    )

}


export default Upload