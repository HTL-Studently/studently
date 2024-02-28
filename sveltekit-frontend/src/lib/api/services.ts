// Helper functions to access the Backend-API

import { Result } from "postcss";

// Please make me dynamic
const fastapiIP = "localhost:8080";

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

    accessToken = "eyJ0eXAiOiJKV1QiLCJub25jZSI6InlEMlNJZC0tRkhkMENDdGQyMThoMk1rR3M5WW9GdmIzbUxJenNIQktKUWciLCJhbGciOiJSUzI1NiIsIng1dCI6IlhSdmtvOFA3QTNVYVdTblU3Yk05blQwTWpoQSIsImtpZCI6IlhSdmtvOFA3QTNVYVdTblU3Yk05blQwTWpoQSJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMvIiwiaWF0IjoxNzA5MTI4NTk2LCJuYmYiOjE3MDkxMjg1OTYsImV4cCI6MTcwOTIxNTI5NiwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhXQUFBQW5HM1kxVjBNK2lhKzNUa0QvalY5ZlZreTcvbkpsWFp6ZllOSHhDSk1LT0swV3E0bEhaSUVMZmRqdEpJR3cyOVBMS1E2SGRjc2hpMnRPSys3djJ0S2V2Q2NyME95Vk1aQUl0QjNSVGJmTjZjPSIsImFtciI6WyJwd2QiLCJyc2EiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggRXhwbG9yZXIiLCJhcHBpZCI6ImRlOGJjOGI1LWQ5ZjktNDhiMS1hOGFkLWI3NDhkYTcyNTA2NCIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiNWFiMjE1MTUtZDE4Yy00ZGM2LTgwMjYtOWE1MzhiZGIzZjczIiwiZmFtaWx5X25hbWUiOiJLVU5PUyIsImdpdmVuX25hbWUiOiJQYW5uYSIsImlkdHlwIjoidXNlciIsImlwYWRkciI6Ijc4LjEwNC4xOTUuMTAiLCJuYW1lIjoiS1VOT1MgUGFubmEsIDVBSElUUyIsIm9pZCI6IjgyOGRjMTU4LTQ3NjUtNDRmMi05MDg4LTZlYWI2N2ZmYTJjNyIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS03NzQ5MTYxMjEtNzg3MzI4ODA2LTkxMTgzMTAzNi0yMzg0MSIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMjAwMDZDMjk0MkQ1IiwicmgiOiIwLkFSQUEtbjRaS3h1T2dFYXlZNDRqZUltMXN3TUFBQUFBQUFBQXdBQUFBQUFBQUFDWEFPQS4iLCJzY3AiOiJEaXJlY3RvcnkuQWNjZXNzQXNVc2VyLkFsbCBEaXJlY3RvcnkuUmVhZC5BbGwgRGlyZWN0b3J5LlJlYWRXcml0ZS5BbGwgRWR1QXNzaWdubWVudHMuUmVhZFdyaXRlIEdyb3VwLlJlYWQuQWxsIEdyb3VwLlJlYWRXcml0ZS5BbGwgb3BlbmlkIHByb2ZpbGUgVXNlci5SZWFkIGVtYWlsIiwic2lnbmluX3N0YXRlIjpbImttc2kiXSwic3ViIjoiNnI3bHE0aU9nRnF2YjcwYW5ieFJmazBkU2luQUZhMy1md0FvVEhXVklWdyIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJFVSIsInRpZCI6IjJiMTk3ZWZhLThlMWItNDY4MC1iMjYzLThlMjM3ODg5YjViMyIsInVuaXF1ZV9uYW1lIjoia3Vub3NwQGVkdS5odGwtdmlsbGFjaC5hdCIsInVwbiI6Imt1bm9zcEBlZHUuaHRsLXZpbGxhY2guYXQiLCJ1dGkiOiJZQXpIa1IzX25FYUE1LUxvR3lRVkFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NjIjpbIkNQMSJdLCJ4bXNfc3NtIjoiMSIsInhtc19zdCI6eyJzdWIiOiJ5T214eU1BZm05SnFabFdHQzg3Nm0wMkZ3T2xkaWxuZXE3SmhEbzNBdTVVIn0sInhtc190Y2R0IjoxMzU0MDEwMjY2LCJ4bXNfdGRiciI6IkVVIn0.NWUyGtjbXrbl8by4neVxwsxpbsIXzID0rhmNtSiyO_Al_0c0bJ1EfGcTWAsSmJr-DGmLQuhOoGGblwkNzBFbbjLFD2uiNm9WrOWd5qnL_yBCXvsf3AJdpC-_LsZotjQyhmnMQKIA_da9ooAPYS3kAFw9OVT8S0uAS3J4HiETrQcD98z12oyvKsO84Qb9Rm912WFQbKWvPRoiTW2YT35mkf2l6HsOv7Q0N34zLSKgfbmTxxaI9xS8dzvL3UqffZmCM7dGltXk93UwuRyYlO0KDRc_4PdgJK0OYSbVaOSxdlPqUinPLQVTrB3HeeUiH5Ru8JCIA-Cnq7cCmc3g2qlG3A"


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
    
    const accessToken = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IkxXY2lnajNKV0tsb3Jlc0dJLXdwNWJlUXJsM2ZZNTFQLV9uZ01Ea1JRWjQiLCJhbGciOiJSUzI1NiIsIng1dCI6ImtXYmthYTZxczh3c1RuQndpaU5ZT2hIYm5BdyIsImtpZCI6ImtXYmthYTZxczh3c1RuQndpaU5ZT2hIYm5BdyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMvIiwiaWF0IjoxNzA4NjI1Nzg4LCJuYmYiOjE3MDg2MjU3ODgsImV4cCI6MTcwODcxMjQ4OCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhXQUFBQUM5TFNQM29yN1FnWXBqaGtid1AzREwzZ2xiOTMyblhWb0hSYklheER6bnBWUmNWZTZsOUtXenlkMGZsSW5SSzAiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIEV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IlNJTcSGScSGIiwiZ2l2ZW5fbmFtZSI6IkVyaWsiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIyMTMuMTYyLjY4LjIzNiIsIm5hbWUiOiJTSU3EhknEhiBFcmlrLCA1QUhJVFMiLCJvaWQiOiI5NmVjMzUwZC1lYTkwLTQwNmItYTZjNi05NDQ2Mzk0OGM3N2QiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtNzc0OTE2MTIxLTc4NzMyODgwNi05MTE4MzEwMzYtMjM5NDEiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzIwMDA2QzI5NDMwRSIsInJoIjoiMC5BUkFBLW40Wkt4dU9nRWF5WTQ0amVJbTFzd01BQUFBQUFBQUF3QUFBQUFBQUFBQ1hBRk0uIiwic2NwIjoiRGlyZWN0b3J5LkFjY2Vzc0FzVXNlci5BbGwgRGlyZWN0b3J5LlJlYWQuQWxsIERpcmVjdG9yeS5SZWFkV3JpdGUuQWxsIEVkdUFzc2lnbm1lbnRzLlJlYWRXcml0ZSBHcm91cC5SZWFkLkFsbCBHcm91cC5SZWFkV3JpdGUuQWxsIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInN1YiI6Ii1weVNJSnBhNnFHRVdqc0pObU1QVU9udHhWdkpGT3hPWGJ3X01ULU0tVkEiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiRVUiLCJ0aWQiOiIyYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMiLCJ1bmlxdWVfbmFtZSI6InNpbWNpY2VAZWR1Lmh0bC12aWxsYWNoLmF0IiwidXBuIjoic2ltY2ljZUBlZHUuaHRsLXZpbGxhY2guYXQiLCJ1dGkiOiIyeTBSNkVQUUJFQ0hfSHljRExnX0FBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NjIjpbIkNQMSJdLCJ4bXNfc3NtIjoiMSIsInhtc19zdCI6eyJzdWIiOiJuUmtLVU0tZ1pta1FhcXYzbG1IVHd1M0VqMDFobnhSU2E4cUVjYVNwSEl3In0sInhtc190Y2R0IjoxMzU0MDEwMjY2LCJ4bXNfdGRiciI6IkVVIn0.V9lOWAilfm1ptGxkk-koc52v13IwRkIsOBIbFLIPk2mnfn5OyCB80Dw9-Y7Lrg5M9qoDA6izB-j_JEMnw7T-yXOUj9Laphn563VNmLtxNA8Cik5-xeSDutyzfLWPjjRaBPS3yI677Fbwsf3FEzx3VCB1alwGoxpFvTHJP3BB9Kmx6pZJa21Qozh26TuEQ4fR7mIZ35esqbz08e0r5JAXFNc92MEyi9svp_9l7-n6oAMsxA-GwKoxhjIbvCqHVQBudzw_MqUjdC8TVQGXlKSurxTv9iOEsc22OcVXqreE6_HaCdtDDvqGTabuWjD4U9nmg2nUkdN_jQZOjEM8Gcd-VA"

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
    const accessToken = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IkxXY2lnajNKV0tsb3Jlc0dJLXdwNWJlUXJsM2ZZNTFQLV9uZ01Ea1JRWjQiLCJhbGciOiJSUzI1NiIsIng1dCI6ImtXYmthYTZxczh3c1RuQndpaU5ZT2hIYm5BdyIsImtpZCI6ImtXYmthYTZxczh3c1RuQndpaU5ZT2hIYm5BdyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMvIiwiaWF0IjoxNzA4NjI1Nzg4LCJuYmYiOjE3MDg2MjU3ODgsImV4cCI6MTcwODcxMjQ4OCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhXQUFBQUM5TFNQM29yN1FnWXBqaGtid1AzREwzZ2xiOTMyblhWb0hSYklheER6bnBWUmNWZTZsOUtXenlkMGZsSW5SSzAiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIEV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IlNJTcSGScSGIiwiZ2l2ZW5fbmFtZSI6IkVyaWsiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIyMTMuMTYyLjY4LjIzNiIsIm5hbWUiOiJTSU3EhknEhiBFcmlrLCA1QUhJVFMiLCJvaWQiOiI5NmVjMzUwZC1lYTkwLTQwNmItYTZjNi05NDQ2Mzk0OGM3N2QiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtNzc0OTE2MTIxLTc4NzMyODgwNi05MTE4MzEwMzYtMjM5NDEiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzIwMDA2QzI5NDMwRSIsInJoIjoiMC5BUkFBLW40Wkt4dU9nRWF5WTQ0amVJbTFzd01BQUFBQUFBQUF3QUFBQUFBQUFBQ1hBRk0uIiwic2NwIjoiRGlyZWN0b3J5LkFjY2Vzc0FzVXNlci5BbGwgRGlyZWN0b3J5LlJlYWQuQWxsIERpcmVjdG9yeS5SZWFkV3JpdGUuQWxsIEVkdUFzc2lnbm1lbnRzLlJlYWRXcml0ZSBHcm91cC5SZWFkLkFsbCBHcm91cC5SZWFkV3JpdGUuQWxsIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInN1YiI6Ii1weVNJSnBhNnFHRVdqc0pObU1QVU9udHhWdkpGT3hPWGJ3X01ULU0tVkEiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiRVUiLCJ0aWQiOiIyYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMiLCJ1bmlxdWVfbmFtZSI6InNpbWNpY2VAZWR1Lmh0bC12aWxsYWNoLmF0IiwidXBuIjoic2ltY2ljZUBlZHUuaHRsLXZpbGxhY2guYXQiLCJ1dGkiOiIyeTBSNkVQUUJFQ0hfSHljRExnX0FBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NjIjpbIkNQMSJdLCJ4bXNfc3NtIjoiMSIsInhtc19zdCI6eyJzdWIiOiJuUmtLVU0tZ1pta1FhcXYzbG1IVHd1M0VqMDFobnhSU2E4cUVjYVNwSEl3In0sInhtc190Y2R0IjoxMzU0MDEwMjY2LCJ4bXNfdGRiciI6IkVVIn0.V9lOWAilfm1ptGxkk-koc52v13IwRkIsOBIbFLIPk2mnfn5OyCB80Dw9-Y7Lrg5M9qoDA6izB-j_JEMnw7T-yXOUj9Laphn563VNmLtxNA8Cik5-xeSDutyzfLWPjjRaBPS3yI677Fbwsf3FEzx3VCB1alwGoxpFvTHJP3BB9Kmx6pZJa21Qozh26TuEQ4fR7mIZ35esqbz08e0r5JAXFNc92MEyi9svp_9l7-n6oAMsxA-GwKoxhjIbvCqHVQBudzw_MqUjdC8TVQGXlKSurxTv9iOEsc22OcVXqreE6_HaCdtDDvqGTabuWjD4U9nmg2nUkdN_jQZOjEM8Gcd-VA"

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
    const accessToken = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IkxXY2lnajNKV0tsb3Jlc0dJLXdwNWJlUXJsM2ZZNTFQLV9uZ01Ea1JRWjQiLCJhbGciOiJSUzI1NiIsIng1dCI6ImtXYmthYTZxczh3c1RuQndpaU5ZT2hIYm5BdyIsImtpZCI6ImtXYmthYTZxczh3c1RuQndpaU5ZT2hIYm5BdyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMvIiwiaWF0IjoxNzA4NjI1Nzg4LCJuYmYiOjE3MDg2MjU3ODgsImV4cCI6MTcwODcxMjQ4OCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhXQUFBQUM5TFNQM29yN1FnWXBqaGtid1AzREwzZ2xiOTMyblhWb0hSYklheER6bnBWUmNWZTZsOUtXenlkMGZsSW5SSzAiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIEV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IlNJTcSGScSGIiwiZ2l2ZW5fbmFtZSI6IkVyaWsiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIyMTMuMTYyLjY4LjIzNiIsIm5hbWUiOiJTSU3EhknEhiBFcmlrLCA1QUhJVFMiLCJvaWQiOiI5NmVjMzUwZC1lYTkwLTQwNmItYTZjNi05NDQ2Mzk0OGM3N2QiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtNzc0OTE2MTIxLTc4NzMyODgwNi05MTE4MzEwMzYtMjM5NDEiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzIwMDA2QzI5NDMwRSIsInJoIjoiMC5BUkFBLW40Wkt4dU9nRWF5WTQ0amVJbTFzd01BQUFBQUFBQUF3QUFBQUFBQUFBQ1hBRk0uIiwic2NwIjoiRGlyZWN0b3J5LkFjY2Vzc0FzVXNlci5BbGwgRGlyZWN0b3J5LlJlYWQuQWxsIERpcmVjdG9yeS5SZWFkV3JpdGUuQWxsIEVkdUFzc2lnbm1lbnRzLlJlYWRXcml0ZSBHcm91cC5SZWFkLkFsbCBHcm91cC5SZWFkV3JpdGUuQWxsIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInN1YiI6Ii1weVNJSnBhNnFHRVdqc0pObU1QVU9udHhWdkpGT3hPWGJ3X01ULU0tVkEiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiRVUiLCJ0aWQiOiIyYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMiLCJ1bmlxdWVfbmFtZSI6InNpbWNpY2VAZWR1Lmh0bC12aWxsYWNoLmF0IiwidXBuIjoic2ltY2ljZUBlZHUuaHRsLXZpbGxhY2guYXQiLCJ1dGkiOiIyeTBSNkVQUUJFQ0hfSHljRExnX0FBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NjIjpbIkNQMSJdLCJ4bXNfc3NtIjoiMSIsInhtc19zdCI6eyJzdWIiOiJuUmtLVU0tZ1pta1FhcXYzbG1IVHd1M0VqMDFobnhSU2E4cUVjYVNwSEl3In0sInhtc190Y2R0IjoxMzU0MDEwMjY2LCJ4bXNfdGRiciI6IkVVIn0.V9lOWAilfm1ptGxkk-koc52v13IwRkIsOBIbFLIPk2mnfn5OyCB80Dw9-Y7Lrg5M9qoDA6izB-j_JEMnw7T-yXOUj9Laphn563VNmLtxNA8Cik5-xeSDutyzfLWPjjRaBPS3yI677Fbwsf3FEzx3VCB1alwGoxpFvTHJP3BB9Kmx6pZJa21Qozh26TuEQ4fR7mIZ35esqbz08e0r5JAXFNc92MEyi9svp_9l7-n6oAMsxA-GwKoxhjIbvCqHVQBudzw_MqUjdC8TVQGXlKSurxTv9iOEsc22OcVXqreE6_HaCdtDDvqGTabuWjD4U9nmg2nUkdN_jQZOjEM8Gcd-VA"

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
    const accessToken = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IkxXY2lnajNKV0tsb3Jlc0dJLXdwNWJlUXJsM2ZZNTFQLV9uZ01Ea1JRWjQiLCJhbGciOiJSUzI1NiIsIng1dCI6ImtXYmthYTZxczh3c1RuQndpaU5ZT2hIYm5BdyIsImtpZCI6ImtXYmthYTZxczh3c1RuQndpaU5ZT2hIYm5BdyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMvIiwiaWF0IjoxNzA4NjI1Nzg4LCJuYmYiOjE3MDg2MjU3ODgsImV4cCI6MTcwODcxMjQ4OCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhXQUFBQUM5TFNQM29yN1FnWXBqaGtid1AzREwzZ2xiOTMyblhWb0hSYklheER6bnBWUmNWZTZsOUtXenlkMGZsSW5SSzAiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIEV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IlNJTcSGScSGIiwiZ2l2ZW5fbmFtZSI6IkVyaWsiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIyMTMuMTYyLjY4LjIzNiIsIm5hbWUiOiJTSU3EhknEhiBFcmlrLCA1QUhJVFMiLCJvaWQiOiI5NmVjMzUwZC1lYTkwLTQwNmItYTZjNi05NDQ2Mzk0OGM3N2QiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtNzc0OTE2MTIxLTc4NzMyODgwNi05MTE4MzEwMzYtMjM5NDEiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzIwMDA2QzI5NDMwRSIsInJoIjoiMC5BUkFBLW40Wkt4dU9nRWF5WTQ0amVJbTFzd01BQUFBQUFBQUF3QUFBQUFBQUFBQ1hBRk0uIiwic2NwIjoiRGlyZWN0b3J5LkFjY2Vzc0FzVXNlci5BbGwgRGlyZWN0b3J5LlJlYWQuQWxsIERpcmVjdG9yeS5SZWFkV3JpdGUuQWxsIEVkdUFzc2lnbm1lbnRzLlJlYWRXcml0ZSBHcm91cC5SZWFkLkFsbCBHcm91cC5SZWFkV3JpdGUuQWxsIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInN1YiI6Ii1weVNJSnBhNnFHRVdqc0pObU1QVU9udHhWdkpGT3hPWGJ3X01ULU0tVkEiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiRVUiLCJ0aWQiOiIyYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMiLCJ1bmlxdWVfbmFtZSI6InNpbWNpY2VAZWR1Lmh0bC12aWxsYWNoLmF0IiwidXBuIjoic2ltY2ljZUBlZHUuaHRsLXZpbGxhY2guYXQiLCJ1dGkiOiIyeTBSNkVQUUJFQ0hfSHljRExnX0FBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NjIjpbIkNQMSJdLCJ4bXNfc3NtIjoiMSIsInhtc19zdCI6eyJzdWIiOiJuUmtLVU0tZ1pta1FhcXYzbG1IVHd1M0VqMDFobnhSU2E4cUVjYVNwSEl3In0sInhtc190Y2R0IjoxMzU0MDEwMjY2LCJ4bXNfdGRiciI6IkVVIn0.V9lOWAilfm1ptGxkk-koc52v13IwRkIsOBIbFLIPk2mnfn5OyCB80Dw9-Y7Lrg5M9qoDA6izB-j_JEMnw7T-yXOUj9Laphn563VNmLtxNA8Cik5-xeSDutyzfLWPjjRaBPS3yI677Fbwsf3FEzx3VCB1alwGoxpFvTHJP3BB9Kmx6pZJa21Qozh26TuEQ4fR7mIZ35esqbz08e0r5JAXFNc92MEyi9svp_9l7-n6oAMsxA-GwKoxhjIbvCqHVQBudzw_MqUjdC8TVQGXlKSurxTv9iOEsc22OcVXqreE6_HaCdtDDvqGTabuWjD4U9nmg2nUkdN_jQZOjEM8Gcd-VA"
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