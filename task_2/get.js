function Get(url) {
    let request = new XMLHttpRequest()
    request.open("GET", url, false)
    request.send(null)
    return request.responseText
}

function includeTable(user) {
    const line = document.createElement("tr");
    const tdId = document.createElement("td");
    const tdName = document.createElement("td");
    const tdEmail = document.createElement("td");
    const tdPassword = document.createElement("td");
    const tdGender = document.createElement("td");
    const tdNationality = document.createElement("td");

    tdId.innerHTML = user.id
    tdName.innerHTML = user.name
    tdEmail.innerHTML = user.email
    tdPassword.innerHTML = user.password
    tdGender.innerHTML = user.gender
    tdNationality.innerHTML = user.nationality

    line.appendChild(tdId);
    line.appendChild(tdName);
    line.appendChild(tdEmail);
    line.appendChild(tdPassword);
    line.appendChild(tdGender);
    line.appendChild(tdNationality);

    return line;
}

function main() {

    let data = Get("http://127.0.0.1:8000/users");
    let users = JSON.parse(data);
    let table = document.getElementById("table");
    users.forEach(user => {
        let line = includeTable(user);
        console.log(user)
        table.appendChild(line);
    });
}

main()