// Helper functions to access the Backend-API

import { Result } from "postcss";

// Please make me dynamic
const fastapiIP = "localhost:8080";

const fix_token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IlFzWHgwbDlrbWtRS3B3Tld0VXRNVEUyWDkwMGY2NDRPVmF0d2tFRDRLWDQiLCJhbGciOiJSUzI1NiIsIng1dCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSIsImtpZCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMvIiwiaWF0IjoxNzEyODE4NTg0LCJuYmYiOjE3MTI4MTg1ODQsImV4cCI6MTcxMjkwNTI4NCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhXQUFBQVZkMG9lVVp1NnhXT0MrbDNPcEFSUUw5M2gxcnhNN2tsWUd0bHBNRXN1TjVXYTdZNEV2WFpYQmp5SzNwcklsL1FvbytqcklxNHk1NVNQcE9UMW1xb1RJbXcyVTU2emttZkdFUGYxT0ZUWGhRPSIsImFtciI6WyJwd2QiLCJyc2EiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggRXhwbG9yZXIiLCJhcHBpZCI6ImRlOGJjOGI1LWQ5ZjktNDhiMS1hOGFkLWI3NDhkYTcyNTA2NCIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiNWFiMjE1MTUtZDE4Yy00ZGM2LTgwMjYtOWE1MzhiZGIzZjczIiwiZmFtaWx5X25hbWUiOiJLVU5PUyIsImdpdmVuX25hbWUiOiJQYW5uYSIsImlkdHlwIjoidXNlciIsImlwYWRkciI6Ijc4LjEwNC4xOTUuMTAiLCJuYW1lIjoiS1VOT1MgUGFubmEsIDVBSElUUyIsIm9pZCI6IjgyOGRjMTU4LTQ3NjUtNDRmMi05MDg4LTZlYWI2N2ZmYTJjNyIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS03NzQ5MTYxMjEtNzg3MzI4ODA2LTkxMTgzMTAzNi0yMzg0MSIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMjAwMDZDMjk0MkQ1IiwicmgiOiIwLkFSQUEtbjRaS3h1T2dFYXlZNDRqZUltMXN3TUFBQUFBQUFBQXdBQUFBQUFBQUFDWEFPQS4iLCJzY3AiOiJEaXJlY3RvcnkuQWNjZXNzQXNVc2VyLkFsbCBEaXJlY3RvcnkuUmVhZC5BbGwgRGlyZWN0b3J5LlJlYWRXcml0ZS5BbGwgRWR1QXNzaWdubWVudHMuUmVhZFdyaXRlIEdyb3VwLlJlYWQuQWxsIEdyb3VwLlJlYWRXcml0ZS5BbGwgb3BlbmlkIHByb2ZpbGUgVXNlci5SZWFkIGVtYWlsIiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiNnI3bHE0aU9nRnF2YjcwYW5ieFJmazBkU2luQUZhMy1md0FvVEhXVklWdyIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJFVSIsInRpZCI6IjJiMTk3ZWZhLThlMWItNDY4MC1iMjYzLThlMjM3ODg5YjViMyIsInVuaXF1ZV9uYW1lIjoia3Vub3NwQGVkdS5odGwtdmlsbGFjaC5hdCIsInVwbiI6Imt1bm9zcEBlZHUuaHRsLXZpbGxhY2guYXQiLCJ1dGkiOiJPMmIzZFM5Y1ZVdW12Nktrc0ZXMEFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NjIjpbIkNQMSJdLCJ4bXNfc3NtIjoiMSIsInhtc19zdCI6eyJzdWIiOiJ5T214eU1BZm05SnFabFdHQzg3Nm0wMkZ3T2xkaWxuZXE3SmhEbzNBdTVVIn0sInhtc190Y2R0IjoxMzU0MDEwMjY2LCJ4bXNfdGRiciI6IkVVIn0.Q_UephW6jkbGYtaxqoFlaIKSYo0D9vaqRdJ6eTLebZclsMTv3ta3-ggECokMsX5MjeyXmNfSBfN1JyxBQS0UXtc6TtHl5VsEdVaPLikkKGo_wrr1jvhuFeICQ5MdUBmsgSi4LLn3DPRFQuk8FWK-jrwbakaIsrtah27V2O1iSmmspzpbW7NsCl4uZOAYTi4sm_1cS0JOyOXX_uIleyVXA8b-J7JM_l6MviRw2D84tWmNWoD8RMyoW7S3HKDlTfvRWHMWARHOvM8f5u5MS6TxBLmIypC3TrtX7MnGhuBuaEdp5l5zXv5YmcoktkQdgU1R4Ec7voz8q8O5Qo82DUtSoA"
// Make me dynamic!
const baseUrl = "http://localhost:8080"

export async function getStudents(full_list: boolean = false, sclass: str = "", id: str = "") {
    const url = `${baseUrl}/students`

    const params = new URLSearchParams({
        full_list: full_list.toString(),
        sclass: sclass,
        id: id,
    });

    try {
        const response = await fetch(`${url}/?${params}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
            credentials: 'include',
        })

        const data = await response.json();
        console.log(data)
        
        return data

    } catch (error) {
    console.error(`Error sending data to ${url}:', ${error}`);
    throw error;
    }
}



export async function get_classes() {
    const url = `http://${fastapiIP}/class`
    const accessToken = fix_token

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