let url = `ws://${window.location.host}/ws/socket-server/`

const chatSocket = new WebSocket(url)

chatSocket.onmessage = function (e) {   
    let data = JSON.parse(e.data)
    console.log("Data: ", data)

    if(data.type === 'chat'){
        let messages = document.getElementById('messages')

        messages.insertAdjacentHTML('beforeend', `<div><p>${data.message}</p></div>`)
    }
}

document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('message_form')
    if (form){
        form.addEventListener('submit', (e) => {
            e.preventDefault()
            let message = e.target.content.value
            chatSocket.send(JSON.stringify({
                'message': message,
            }));
            form.submit()
        })
    }
    
 }, true);