import { writable } from 'svelte/store';
import { get_profile } from "../api/services.ts"


export const cookiesJWT = writable()


let accessToken = "eyJ0eXAiOiJKV1QiLCJub25jZSI6ImJwOTNwZUc5R013SktSWnJIU1NTdmp3M2I1eC1mcnNsREc2SzhlSVVGYXciLCJhbGciOiJSUzI1NiIsIng1dCI6IlhSdmtvOFA3QTNVYVdTblU3Yk05blQwTWpoQSIsImtpZCI6IlhSdmtvOFA3QTNVYVdTblU3Yk05blQwTWpoQSJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8yYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMvIiwiaWF0IjoxNzEwOTQ5OTg4LCJuYmYiOjE3MTA5NDk5ODgsImV4cCI6MTcxMTAzNjY4OCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhXQUFBQVVETnRVRVNJakFpQlE3eUdjNXNmeVp1MTlRTVltNnorZXUyQnJNNmlpMjMveHZxbVdESWV6bGdSaGhzV1dGVHYiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IkdyYXBoIEV4cGxvcmVyIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IlNJTcSGScSGIiwiZ2l2ZW5fbmFtZSI6IkVyaWsiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIyMTMuMTYyLjczLjEzMSIsIm5hbWUiOiJTSU3EhknEhiBFcmlrLCA1QUhJVFMiLCJvaWQiOiI5NmVjMzUwZC1lYTkwLTQwNmItYTZjNi05NDQ2Mzk0OGM3N2QiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtNzc0OTE2MTIxLTc4NzMyODgwNi05MTE4MzEwMzYtMjM5NDEiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzIwMDA2QzI5NDMwRSIsInJoIjoiMC5BUkFBLW40Wkt4dU9nRWF5WTQ0amVJbTFzd01BQUFBQUFBQUF3QUFBQUFBQUFBQ1hBRk0uIiwic2NwIjoiRGlyZWN0b3J5LkFjY2Vzc0FzVXNlci5BbGwgRGlyZWN0b3J5LlJlYWQuQWxsIERpcmVjdG9yeS5SZWFkV3JpdGUuQWxsIEVkdUFzc2lnbm1lbnRzLlJlYWRXcml0ZSBHcm91cC5SZWFkLkFsbCBHcm91cC5SZWFkV3JpdGUuQWxsIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInN1YiI6Ii1weVNJSnBhNnFHRVdqc0pObU1QVU9udHhWdkpGT3hPWGJ3X01ULU0tVkEiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiRVUiLCJ0aWQiOiIyYjE5N2VmYS04ZTFiLTQ2ODAtYjI2My04ZTIzNzg4OWI1YjMiLCJ1bmlxdWVfbmFtZSI6InNpbWNpY2VAZWR1Lmh0bC12aWxsYWNoLmF0IiwidXBuIjoic2ltY2ljZUBlZHUuaHRsLXZpbGxhY2guYXQiLCJ1dGkiOiJRbndFTmFhT2hVT0NqaklYZmxOdUFBIiwidmVyIjoiMS4wIiwid2lkcyI6WyJiNzlmYmY0ZC0zZWY5LTQ2ODktODE0My03NmIxOTRlODU1MDkiXSwieG1zX2NjIjpbIkNQMSJdLCJ4bXNfc3NtIjoiMSIsInhtc19zdCI6eyJzdWIiOiJuUmtLVU0tZ1pta1FhcXYzbG1IVHd1M0VqMDFobnhSU2E4cUVjYVNwSEl3In0sInhtc190Y2R0IjoxMzU0MDEwMjY2LCJ4bXNfdGRiciI6IkVVIn0.OALAu3s9Vkmw1ZOWPE3e-YuMVGpE3R5Nd7jtpdn48WIRE0hWdGprpm4chrYFqU9LQpCYONcUbEVjqMwSlSYKi1ZCoKhTHc-UDrjbpjZLPFapYf9M8o7D3MEo9JQcVl_F6VHEX0S9g_0YJ_acyctZWGQWyvDYHKDTmGOxXWJngNNOq3rbWqUOp6jccE7OYOO4qDoDexV_MKWeO6u0r6mzoSbzBZyrnLDYmyyxqIxCWFuoQiy0zW9hSO2mK7bUt28AdESw8RZ8fm-CzFoUdJ3vPKt7KD4y178y8_tqzFaxpsG41qtg1usJzv2lcAopSEMz9bAGL3qJjAbQKPbQWAmdUw"

let profile = await get_profile(accessToken);
profile = profile.message.profile;

export const user = writable({
    disabled: profile.disabled,
    identifier: profile.identifier,
    username: profile.username,
    firstname: profile.firstname,
    lastname: profile.lastname,
    email: profile.email,
    expires: profile.expires,
    created: profile.created,
    sclass: profile.sclass,
    type: profile.type,
    owned_objects: profile.owned_objects,
    owned_payments: profile.owned_payments,
});