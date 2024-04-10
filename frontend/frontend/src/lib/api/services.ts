// Helper functions to access the Backend-API

import { Result } from "postcss";

// Please make me dynamic
const fastapiIP = "localhost:8080";

const fix_token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6InRDb1R0NFJHb2ZPdWotNk45bF92eW1kZ01QMGFnRjh2emhsOTFUNVBSbGMiLCJhbGciOiJSUzI1NiIsIng1dCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSIsImtpZCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMvIiwiaWF0IjoxNzEyNzM2MDEwLCJuYmYiOjE3MTI3MzYwMTAsImV4cCI6MTcxMjgyMjcxMCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhXQUFBQUdHczlnU3NIRHpQZnN6MGR1RExkQWVBelNIRklvb1czL2tzVzl1b0xnSlhzQmJIR1NIY3kvalhYSDNUbXNKVE8iLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIEV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IlNJTcSGScSGIiwiZ2l2ZW5fbmFtZSI6IkVyaWsiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiI3OC4xMDQuMTk1LjEwIiwibmFtZSI6IlNJTcSGScSGIEVyaWssIDVBSElUUyIsIm9pZCI6Ijk2ZWMzNTBkLWVhOTAtNDA2Yi1hNmM2LTk0NDYzOTQ4Yzc3ZCIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS03NzQ5MTYxMjEtNzg3MzI4ODA2LTkxMTgzMTAzNi0yMzk0MSIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMjAwMDZDMjk0MzBFIiwicmgiOiIwLkFSQUEtbjRaS3h1T2dFYXlZNDRqZUltMXN3TUFBQUFBQUFBQXdBQUFBQUFBQUFDWEFGTS4iLCJzY3AiOiJEaXJlY3RvcnkuQWNjZXNzQXNVc2VyLkFsbCBEaXJlY3RvcnkuUmVhZC5BbGwgRGlyZWN0b3J5LlJlYWRXcml0ZS5BbGwgRWR1QXNzaWdubWVudHMuUmVhZFdyaXRlIEdyb3VwLlJlYWQuQWxsIEdyb3VwLlJlYWRXcml0ZS5BbGwgb3BlbmlkIHByb2ZpbGUgVXNlci5SZWFkIGVtYWlsIiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiLXB5U0lKcGE2cUdFV2pzSk5tTVBVT250eFZ2SkZPeE9YYndfTVQtTS1WQSIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJFVSIsInRpZCI6IjJiMTk3ZWZhLThlMWItNDY4MC1iMjYzLThlMjM3ODg5YjViMyIsInVuaXF1ZV9uYW1lIjoic2ltY2ljZUBlZHUuaHRsLXZpbGxhY2guYXQiLCJ1cG4iOiJzaW1jaWNlQGVkdS5odGwtdmlsbGFjaC5hdCIsInV0aSI6IkdnSTFFM3lpckUtYzVQRUVaR3d3QUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfY2MiOlsiQ1AxIl0sInhtc19zc20iOiIxIiwieG1zX3N0Ijp7InN1YiI6Im5Sa0tVTS1nWm1rUWFxdjNsbUhUd3UzRWowMWhueFJTYThxRWNhU3BISXcifSwieG1zX3RjZHQiOjEzNTQwMTAyNjYsInhtc190ZGJyIjoiRVUifQ.S3i2PkU6gf7PgbzqEux1RDzQDlH1RGcZxfES-GNIcJ8ga17Ex_VAS1aktEp6PHvpITCuVd-cl7pSFsC8lKSQFPTdM2VWTKporiaLToBHQZ__PSzY-1-HDcXOBc1K-exf-BiNoDBQ_b-MrKwexyElPs0EL09ZSvcyBYhlx5FSJkhvu3O7e2rpwtE7YIjDWh2TgB65jbOawulKmBXBhFs6T-cJtix13F_AMDeLCRObvqUALYe8n0NJL9ijewwVPB966qhqhjeeXsAfpjDAHdC3p46Cmc9gnbv52vqbimXD9yHcy7BTcJcoC78cbkk3e0HBOSmXEhDeyjD1m9tH9ewoVw"

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