
const chatInput=document.querySelector(".chat-input textarea");
const sendChatBtn = document.querySelector(".chat-input span");
const chatbox = document.querySelector(".chat-list")
let msg

const createChatList =(message,className) =>{
    const chatlist = document.createElement("li");
    chatlist.classList.add("chatt",className);
    let chatContent = className === "chat-outgoing" ? `<div class="ch"><p>${message}</p></div>`:`<i class="fa-solid fa-robot fa-xl"></i><div class="ch"><p>You probably Have : ${message}</p></div>`;
    chatlist.innerHTML= chatContent;
    console.log("Executed bruh");
    return chatlist;
}
const handleChat=()=>{
    msg=chatInput.value.trim();
    if(!msg) return;
    console.log(msg)
    chatbox.appendChild(createChatList(msg,"chat-outgoing"));
    const socket = io.connect('http://127.0.0.1:5000');
    socket.emit('data_from_client', { data: msg });
    socket.on('json_response', function(data) {
    // Handle the JSON data received from the server
    console.log(data.message)
    chatbox.appendChild(createChatList(data.message,"chat-incoming"))
        });
    

}

sendChatBtn.addEventListener("click",handleChat);