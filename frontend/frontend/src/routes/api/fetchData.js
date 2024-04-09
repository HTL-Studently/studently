export async function get(request) {


    const accessToken = event.cookies.get("accessToken"); 


    const data = await fetchExternalData();
    return {
       body: data
    };
   }