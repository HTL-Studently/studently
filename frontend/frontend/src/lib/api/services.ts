// Helper functions to access the Backend-API

import { Result } from "postcss";

// Please make me dynamic
const fastapiIP = "localhost:8080";

const fix_token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6InFFaGhKVjVBel9wRG1IR0VQNldhT1VVSDB5OC1neWpoMHpaVEV2NzFRUDAiLCJhbGciOiJSUzI1NiIsIng1dCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSIsImtpZCI6InEtMjNmYWxldlpoaEQzaG05Q1Fia1A1TVF5VSJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMvIiwiaWF0IjoxNzEyNjk1MDc0LCJuYmYiOjE3MTI2OTUwNzQsImV4cCI6MTcxMjc4MTc3NSwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhXQUFBQWJKSU9HM3I1ZEpPbjJ3T3V2UGF2ZVNBNG9uRTVCOWxKN2l0Um5hZWpKdEJ2K0hLMzZkaU9idk54L2tEYVFkSkpobk1OdS9pbG4wZ2VUalIwRzZkdUpiTENSVGtQUGlveEl2bTdPVmsrZUpRPSIsImFtciI6WyJwd2QiLCJyc2EiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggRXhwbG9yZXIiLCJhcHBpZCI6ImRlOGJjOGI1LWQ5ZjktNDhiMS1hOGFkLWI3NDhkYTcyNTA2NCIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiNWFiMjE1MTUtZDE4Yy00ZGM2LTgwMjYtOWE1MzhiZGIzZjczIiwiZmFtaWx5X25hbWUiOiJLVU5PUyIsImdpdmVuX25hbWUiOiJQYW5uYSIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjIxMy4xNjIuODEuMTYzIiwibmFtZSI6IktVTk9TIFBhbm5hLCA1QUhJVFMiLCJvaWQiOiI4MjhkYzE1OC00NzY1LTQ0ZjItOTA4OC02ZWFiNjdmZmEyYzciLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtNzc0OTE2MTIxLTc4NzMyODgwNi05MTE4MzEwMzYtMjM4NDEiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzIwMDA2QzI5NDJENSIsInJoIjoiMC5BUkFBLW40Wkt4dU9nRWF5WTQ0amVJbTFzd01BQUFBQUFBQUF3QUFBQUFBQUFBQ1hBT0EuIiwic2NwIjoiRGlyZWN0b3J5LkFjY2Vzc0FzVXNlci5BbGwgRGlyZWN0b3J5LlJlYWQuQWxsIERpcmVjdG9yeS5SZWFkV3JpdGUuQWxsIEVkdUFzc2lnbm1lbnRzLlJlYWRXcml0ZSBHcm91cC5SZWFkLkFsbCBHcm91cC5SZWFkV3JpdGUuQWxsIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6IjZyN2xxNGlPZ0ZxdmI3MGFuYnhSZmswZFNpbkFGYTMtZndBb1RIV1ZJVnciLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiRVUiLCJ0aWQiOiIyYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMiLCJ1bmlxdWVfbmFtZSI6Imt1bm9zcEBlZHUuaHRsLXZpbGxhY2guYXQiLCJ1cG4iOiJrdW5vc3BAZWR1Lmh0bC12aWxsYWNoLmF0IiwidXRpIjoidjQtLUktX1ZfVUsyc0FxUzVDNXdBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYyI6WyJDUDEiXSwieG1zX3NzbSI6IjEiLCJ4bXNfc3QiOnsic3ViIjoieU9teHlNQWZtOUpxWmxXR0M4NzZtMDJGd09sZGlsbmVxN0poRG8zQXU1VSJ9LCJ4bXNfdGNkdCI6MTM1NDAxMDI2NiwieG1zX3RkYnIiOiJFVSJ9.0D6C8TFYqUmvNe4NdaOukBDpt_VitG1Q9JhUUI--w6vxsLrYl9Jcr7jHcBgKDimBryMD18DIgKyX3FNvdi6m1zbzJNiVpFLvd1XymgKSeiZPgcmaR789ZySFVxOVUd1KwA-9NLjaBnvIo438YUGbdhBjQnuq7tkJKEKvOmxlJPv8wB6KTUm1-hS876Z41Bd8cfGEXH1K3JmUgDwHQ3PlCfKtkfDa-26rp7VA2suJ2yRAgYa6LvVB10LZ_eC6yqJlpduv62zWlPu_na95zkHAvwI5floQ0Sqv-NqZyDh3V1rttIYFTpN0Sd_sc9Gfatb3WCLs53FV56ymF7e-r2-PDw"

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