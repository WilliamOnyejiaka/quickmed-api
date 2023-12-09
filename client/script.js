
async function signUp(){

    const res = await fetch("http://127.0.0.1:5000/api/auth/sign-up",{
        method: "POST",
        credentials: "include",
        body:JSON.stringify({
            "firstName": "William",
            "lastName": "Wonder",
            "username": "user",
            "email": "email@email.com",
            "password": "password",
            "phoneNumber": "09026405140"
        }),
        headers:{
            "content-type":"application/json"
        }
    });

    const data = await res.json();

    console.log(data);
}

signUp()