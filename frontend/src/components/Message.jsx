import ReactMarkdown from "react-markdown"


function Message({text,type}){


return (

<div
className={
type==="user"
?
"bg-blue-100 p-3 rounded"
:
"bg-gray-100 p-3 rounded"
}
>


<ReactMarkdown>

{text}

</ReactMarkdown>


</div>

)


}


export default Message