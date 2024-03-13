// Helper functions to access the Backend-API

import { Result } from "postcss";

// Please make me dynamic
const fastapiIP = "localhost:8080";

const fix_token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IkpBWk9POFZYTmdaVHMwVVZrWXFhbFp4dFRmUGFGQ1d6WHRUaUpXbkEzb28iLCJhbGciOiJSUzI1NiIsIng1dCI6IlhSdmtvOFA3QTNVYVdTblU3Yk05blQwTWpoQSIsImtpZCI6IlhSdmtvOFA3QTNVYVdTblU3Yk05blQwTWpoQSJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMvIiwiaWF0IjoxNzEwMzMzMDYxLCJuYmYiOjE3MTAzMzMwNjEsImV4cCI6MTcxMDQxOTc2MSwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhXQUFBQThXQWdKbmRqNTVBUndRaWkxQ2ZtblVycGRrVEhRclJBZXdzclBIbE9mcHJPRjIyaUloc2ROVnFkKzZNMDAvSHgiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIEV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IlNJTcSGScSGIiwiZ2l2ZW5fbmFtZSI6IkVyaWsiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiI3OC4xMDQuMTk1LjEwIiwibmFtZSI6IlNJTcSGScSGIEVyaWssIDVBSElUUyIsIm9pZCI6Ijk2ZWMzNTBkLWVhOTAtNDA2Yi1hNmM2LTk0NDYzOTQ4Yzc3ZCIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS03NzQ5MTYxMjEtNzg3MzI4ODA2LTkxMTgzMTAzNi0yMzk0MSIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMjAwMDZDMjk0MzBFIiwicmgiOiIwLkFSQUEtbjRaS3h1T2dFYXlZNDRqZUltMXN3TUFBQUFBQUFBQXdBQUFBQUFBQUFDWEFGTS4iLCJzY3AiOiJEaXJlY3RvcnkuQWNjZXNzQXNVc2VyLkFsbCBEaXJlY3RvcnkuUmVhZC5BbGwgRGlyZWN0b3J5LlJlYWRXcml0ZS5BbGwgRWR1QXNzaWdubWVudHMuUmVhZFdyaXRlIEdyb3VwLlJlYWQuQWxsIEdyb3VwLlJlYWRXcml0ZS5BbGwgb3BlbmlkIHByb2ZpbGUgVXNlci5SZWFkIGVtYWlsIiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiLXB5U0lKcGE2cUdFV2pzSk5tTVBVT250eFZ2SkZPeE9YYndfTVQtTS1WQSIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJFVSIsInRpZCI6IjJiMTk3ZWZhLThlMWItNDY4MC1iMjYzLThlMjM3ODg5YjViMyIsInVuaXF1ZV9uYW1lIjoic2ltY2ljZUBlZHUuaHRsLXZpbGxhY2guYXQiLCJ1cG4iOiJzaW1jaWNlQGVkdS5odGwtdmlsbGFjaC5hdCIsInV0aSI6IjhYOVIxNFVyZzBTNlp3bE41SDZLQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfY2MiOlsiQ1AxIl0sInhtc19zc20iOiIxIiwieG1zX3N0Ijp7InN1YiI6Im5Sa0tVTS1nWm1rUWFxdjNsbUhUd3UzRWowMWhueFJTYThxRWNhU3BISXcifSwieG1zX3RjZHQiOjEzNTQwMTAyNjYsInhtc190ZGJyIjoiRVUifQ.j_WLBasF6L4QaNg2fjWQHyv-LaQUQeoRF6vdqvXyZ6Qd37DA6EYID6q7Yt6DeAL0dsrjDqM5BX51-9XpvQbYTWpsu7QKBwlKfobFhzh7gXQY1S6aWkFBekfMF3OLucH2bRmPKpJbqM0UhqvXSt65Eyf8oHT_yr8XY8fz9MYM2HDE-DwrAnsVhNhFENrsuoCuhuhBsF3Z1g0OXEp9tmCCCVmooBGAAfr-kCrHnITQqT4xkNXr7Mw4rv-nnzRrx4DZyBieP_upfTeFVej47QcwL14qFAM4T5XXyRku_2ZYIUw4wz_vKrYx9y6XxtFMD2qqg8JtHlAxhn3u7Xtfnlr_Tw"

export async function sendUserLogin(accessToken: any, idToken: any) {
    const url = `http://${fastapiIP}/signin`

    const loginData = {
        "accessToken": accessToken,
        "idToken": idToken,
    }

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(loginData)
        })

        return response;

    } catch (error) {
    console.error(`Error sending data to ${url}:', ${error}`);
    throw error;
    }
}


export async function get_profile(accessToken: any) {
    console.log("TRYING TO GET PROFILE")
    const url = `http://${fastapiIP}/profile`

    accessToken = fix_token

    const loginData = {
        "access_token": accessToken,
    }

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(loginData)
        })

        const data = await response.json();

        return data


    } catch (error) {
    console.error(`Error sending data to ${url}:', ${error}`);
    throw error;
    }
}

export async function upload_paymentconfirm(formData) {
    const url = `http://${fastapiIP}/confirmpay`
    
    const accessToken = fix_token

    formData.append("access_token", accessToken)

    try {
        const response = fetch('http://localhost:8080/confirmpay', {
            method: 'POST',
            headers: {
                'Accept': 'multipart/form-data',
            },
            body: formData
        })


    } catch (error) {
    console.error(`Error sending data to ${url}:', ${error}`);
    throw error;
    }

}

export async function get_classes() {
    const url = `http://${fastapiIP}/class`
    const accessToken = fix_token
    const loginData = {
        "access_token": accessToken,
    }

    try {
        const response = await fetch(`http://${fastapiIP}/class`, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                access_token: accessToken
            }),
        });

        const data = await response.json();

        return data

    } catch (error) {
    console.error(`Error sending data to ${url}:', ${error}`);
    throw error;
    }

}

export async function get_students(search_val) {
    const url = `http://${fastapiIP}/student`
    const accessToken = fix_token
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                access_token: accessToken,
                search_par: "sclass",
                search_val: search_val
            }),
        });

        const data = await response.json();

        return data

    } catch (error) {
    console.error(`Error sending data to ${url}:', ${error}`);
    throw error;
    }
}

export async function assign_payment(paymentFormData) {
    const url = `http://${fastapiIP}/payment`

    const accessToken = fix_token

    
    paymentFormData.access_token = accessToken


    try {
        const response = fetch(url, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                access_token: accessToken,
                disabled: "Test",
                name: "Test",
                author: "Test",
                target_type: "Test",
                target: "5AHITS",
                product: "Test",
                confirmation: null,
                payed: false,
                cost: 123,
                iban: "Test",
                bic: "Test",
                start_date: new Date().toISOString(),
                due_date: new Date().toISOString(),
                expires: new Date(new Date().getTime() + (365 * 24 * 60 * 60 * 1000)).toISOString(),
            })
        })

        console.log(response)


    } catch (error) {
    console.error(`Error sending data to ${url}:', ${error}`);
    throw error;
    }

}