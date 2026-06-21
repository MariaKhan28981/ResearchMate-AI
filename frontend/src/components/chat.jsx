import { useState } from "react"
import client from "../api/client"
import Message from "./Message"



function Chat(){


    const [question,setQuestion] = useState("")

    const [messages,setMessages] = useState([])

    const [loading,setLoading] = useState(false)



    async function ask(){


        if(!question.trim()) return



        const userMessage = question



        setMessages(prev => [

            ...prev,

            {
                text:userMessage,
                type:"user"
            }

        ])


        setQuestion("")


        try{


            setLoading(true)



            const response = await client.post(

                "/chat",

                {
                    question:userMessage
                }

            )



            setMessages(prev => [

                ...prev,

                {
                    text:response.data.answer,
                    type:"ai"
                }

            ])



        }

        catch(error){

            console.log(error)


            setMessages(prev => [

                ...prev,

                {
                    text:"Something went wrong.",
                    type:"ai"
                }

            ])

        }


        finally{

            setLoading(false)

        }

    }





    return (

        <div>


            <div className="space-y-3 mb-5">


                {

                messages.map(

                    (m,i)=>(

                        <Message

                            key={i}

                            text={m.text}

                            type={m.type}

                        />

                    )

                )

                }


                {
                    loading &&
                    <p>
                        Thinking...
                    </p>
                }


            </div>




            <input


                id="chat-question"

                name="question"

                placeholder="Ask something about your paper..."


                value={question}


                onChange={
                    e=>setQuestion(e.target.value)
                }


                className="border p-2 w-full"

            />



            <button


                type="button"


                onClick={ask}


                className="mt-3 bg-black text-white px-5 py-2 rounded"


            >

                Ask


            </button>



        </div>

    )

}


export default Chat