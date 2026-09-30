const input =
    document.getElementById("user-input");

const chatBox =
    document.getElementById("chat-box");

const sendButton =
    document.getElementById("send-button");


function addMessage(message, sender) {

    const messageDiv =
        document.createElement("div");

    messageDiv.classList.add(
        "message",
        sender
    );

    if (sender === "bot") {

        messageDiv.innerHTML = `
            <div class="message-name">
                AI Assistant
            </div>

            <div>${formatText(message)}</div>
        `;

    } else {

        messageDiv.textContent = message;
    }

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop =
        chatBox.scrollHeight;
}


function formatText(text) {

    return text
        .replace(/\n/g, "<br>")
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
}


async function sendMessage() {

    const message =
        input.value.trim();

    if (!message) {
        return;
    }

    addMessage(
        message,
        "user"
    );

    input.value = "";

    sendButton.disabled = true;

    const loading = document.createElement("div");

    loading.classList.add(
        "message",
        "bot"
    );

    loading.textContent =
        "Thinking...";

    chatBox.appendChild(loading);

    chatBox.scrollTop =
        chatBox.scrollHeight;


    try {

        const response =
            await fetch("/chat", {

                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    message: message
                })
            });


        const data =
            await response.json();


        loading.remove();


        if (data.reply) {

            addMessage(
                data.reply,
                "bot"
            );

        } else {

            addMessage(
                "Sorry, something went wrong.",
                "bot"
            );
        }


    } catch (error) {

        loading.remove();

        addMessage(
            "Unable to connect to the server.",
            "bot"
        );

        console.error(error);

    }


    sendButton.disabled = false;

    input.focus();
}


function quickMessage(message) {

    input.value = message;

    sendMessage();
}


async function requestAgent() {

    const issue =
        prompt(
            "Please briefly describe your issue:"
        );


    if (!issue) {
        return;
    }


    try {

        const response =
            await fetch(
                "/create-ticket",
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        issue: issue
                    })
                }
            );


        const data =
            await response.json();


        addMessage(
            data.message,
            "bot"
        );


    } catch (error) {

        addMessage(
            "Unable to create the support ticket.",
            "bot"
        );

    }
}


input.addEventListener(
    "keypress",
    function(event) {

        if (event.key === "Enter") {

            sendMessage();

        }

    }
);