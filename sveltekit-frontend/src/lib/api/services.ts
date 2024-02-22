// Helper functions to access the Backend-API

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

	accessToken = "eyJ0eXAiOiJKV1QiLCJub25jZSI6IkxXY2lnajNKV0tsb3Jlc0dJLXdwNWJlUXJsM2ZZNTFQLV9uZ01Ea1JRWjQiLCJhbGciOiJSUzI1NiIsIng1dCI6ImtXYmthYTZxczh3c1RuQndpaU5ZT2hIYm5BdyIsImtpZCI6ImtXYmthYTZxczh3c1RuQndpaU5ZT2hIYm5BdyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMvIiwiaWF0IjoxNzA4NjI1Nzg4LCJuYmYiOjE3MDg2MjU3ODgsImV4cCI6MTcwODcxMjQ4OCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhXQUFBQUM5TFNQM29yN1FnWXBqaGtid1AzREwzZ2xiOTMyblhWb0hSYklheER6bnBWUmNWZTZsOUtXenlkMGZsSW5SSzAiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIEV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IlNJTcSGScSGIiwiZ2l2ZW5fbmFtZSI6IkVyaWsiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIyMTMuMTYyLjY4LjIzNiIsIm5hbWUiOiJTSU3EhknEhiBFcmlrLCA1QUhJVFMiLCJvaWQiOiI5NmVjMzUwZC1lYTkwLTQwNmItYTZjNi05NDQ2Mzk0OGM3N2QiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtNzc0OTE2MTIxLTc4NzMyODgwNi05MTE4MzEwMzYtMjM5NDEiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzIwMDA2QzI5NDMwRSIsInJoIjoiMC5BUkFBLW40Wkt4dU9nRWF5WTQ0amVJbTFzd01BQUFBQUFBQUF3QUFBQUFBQUFBQ1hBRk0uIiwic2NwIjoiRGlyZWN0b3J5LkFjY2Vzc0FzVXNlci5BbGwgRGlyZWN0b3J5LlJlYWQuQWxsIERpcmVjdG9yeS5SZWFkV3JpdGUuQWxsIEVkdUFzc2lnbm1lbnRzLlJlYWRXcml0ZSBHcm91cC5SZWFkLkFsbCBHcm91cC5SZWFkV3JpdGUuQWxsIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInN1YiI6Ii1weVNJSnBhNnFHRVdqc0pObU1QVU9udHhWdkpGT3hPWGJ3X01ULU0tVkEiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiRVUiLCJ0aWQiOiIyYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMiLCJ1bmlxdWVfbmFtZSI6InNpbWNpY2VAZWR1Lmh0bC12aWxsYWNoLmF0IiwidXBuIjoic2ltY2ljZUBlZHUuaHRsLXZpbGxhY2guYXQiLCJ1dGkiOiIyeTBSNkVQUUJFQ0hfSHljRExnX0FBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NjIjpbIkNQMSJdLCJ4bXNfc3NtIjoiMSIsInhtc19zdCI6eyJzdWIiOiJuUmtLVU0tZ1pta1FhcXYzbG1IVHd1M0VqMDFobnhSU2E4cUVjYVNwSEl3In0sInhtc190Y2R0IjoxMzU0MDEwMjY2LCJ4bXNfdGRiciI6IkVVIn0.V9lOWAilfm1ptGxkk-koc52v13IwRkIsOBIbFLIPk2mnfn5OyCB80Dw9-Y7Lrg5M9qoDA6izB-j_JEMnw7T-yXOUj9Laphn563VNmLtxNA8Cik5-xeSDutyzfLWPjjRaBPS3yI677Fbwsf3FEzx3VCB1alwGoxpFvTHJP3BB9Kmx6pZJa21Qozh26TuEQ4fR7mIZ35esqbz08e0r5JAXFNc92MEyi9svp_9l7-n6oAMsxA-GwKoxhjIbvCqHVQBudzw_MqUjdC8TVQGXlKSurxTv9iOEsc22OcVXqreE6_HaCdtDDvqGTabuWjD4U9nmg2nUkdN_jQZOjEM8Gcd-VA"

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