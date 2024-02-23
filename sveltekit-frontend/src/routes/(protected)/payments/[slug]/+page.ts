export function load({params}) {
    
    console.log(params)
    
    return{
        title:params.slug
    }
}