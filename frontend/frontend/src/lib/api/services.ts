// Helper functions to access the Backend-API

import { Result } from "postcss";

// Please make me dynamic
const fastapiIP = "localhost:8080";

const fix_token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IkU4SnJSWWhjTFlaS3lZcWk5UlVobng1cEg2Z0ZKZFI2d2pMdnJnMEpQYkUiLCJhbGciOiJSUzI1NiIsIng1dCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSIsImtpZCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMvIiwiaWF0IjoxNzEyODcxNTkzLCJuYmYiOjE3MTI4NzE1OTMsImV4cCI6MTcxMjk1ODI5MywiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhXQUFBQVFhb0ZOS0o0dzBKcDByWVQyZXJRd0J0R0p0aDJkZVZrZEl2UXA0N0xsQ1NtYXBwbFR2QU5GOWVpaGIreEtTZ3IiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIEV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IlNJTcSGScSGIiwiZ2l2ZW5fbmFtZSI6IkVyaWsiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIyMTMuMTYyLjczLjU4IiwibmFtZSI6IlNJTcSGScSGIEVyaWssIDVBSElUUyIsIm9pZCI6Ijk2ZWMzNTBkLWVhOTAtNDA2Yi1hNmM2LTk0NDYzOTQ4Yzc3ZCIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS03NzQ5MTYxMjEtNzg3MzI4ODA2LTkxMTgzMTAzNi0yMzk0MSIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMjAwMDZDMjk0MzBFIiwicmgiOiIwLkFSQUEtbjRaS3h1T2dFYXlZNDRqZUltMXN3TUFBQUFBQUFBQXdBQUFBQUFBQUFDWEFGTS4iLCJzY3AiOiJEaXJlY3RvcnkuQWNjZXNzQXNVc2VyLkFsbCBEaXJlY3RvcnkuUmVhZC5BbGwgRGlyZWN0b3J5LlJlYWRXcml0ZS5BbGwgRWR1QXNzaWdubWVudHMuUmVhZFdyaXRlIEdyb3VwLlJlYWQuQWxsIEdyb3VwLlJlYWRXcml0ZS5BbGwgb3BlbmlkIHByb2ZpbGUgVXNlci5SZWFkIGVtYWlsIiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiLXB5U0lKcGE2cUdFV2pzSk5tTVBVT250eFZ2SkZPeE9YYndfTVQtTS1WQSIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJFVSIsInRpZCI6IjJiMTk3ZWZhLThlMWItNDY4MC1iMjYzLThlMjM3ODg5YjViMyIsInVuaXF1ZV9uYW1lIjoic2ltY2ljZUBlZHUuaHRsLXZpbGxhY2guYXQiLCJ1cG4iOiJzaW1jaWNlQGVkdS5odGwtdmlsbGFjaC5hdCIsInV0aSI6Il9ENTZyV1pVRFV1LTR5VWxHMkh0QUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfY2MiOlsiQ1AxIl0sInhtc19zc20iOiIxIiwieG1zX3N0Ijp7InN1YiI6Im5Sa0tVTS1nWm1rUWFxdjNsbUhUd3UzRWowMWhueFJTYThxRWNhU3BISXcifSwieG1zX3RjZHQiOjEzNTQwMTAyNjYsInhtc190ZGJyIjoiRVUifQ.fbQ2E3zIwZTR5h_wW7WFeEPlWbtsh39-oXE1nRhYlgnEIajj_eVlaBTNC43TqGyU-7xJtvSwll2Maav2vmx8jNC6I0UjhGJZ4el4PorzJCChDl6d8P5cVn4gkvMHI7LX9PrZBaH-QMa2pEn9uP26MjyoArwGCyz-2njowxFhyrcp7eqbRDYi7wWLubZ7U97n2EFQdeTaebemEHwyhQJUY2qGYn7KTF1Q0nQe3_Wrs10P0fOk2hTzIbbgU_77ON-2girO06HbqoPGyvEKjU8_JtlL0wae6cU_vXX8eQ57VFurvmhIgKfDeKMQEyB_n6vKHB7AdKyI2mO_L6-y-NWJzQ"
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