import axios from "axios";

const baseURL = "http://localhost:5000";

export default function getMentions(name){

    return axios.get(`${baseURL}/api/v1.0/mentions`, {
        params:{
            name: name
        }
    })

}