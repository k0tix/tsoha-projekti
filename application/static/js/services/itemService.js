import axios from 'axios'
const baseUrl = 'http://127.0.0.1:5000/api/items/'

const getAll = () => {
    const request = axios.get(baseUrl)
    return request.then(response => response.data)
}

const create = (newItem) => {
    const request = axios.post(baseUrl, newItem)
    return request.then(response => response.data)
}

const update = (id, newPrice) => {
    console.log(newPrice)
    const request = axios.put(`${baseUrl}${id}/`, {price: newPrice})
    return request.then(response => response.data)
}

export default {
    getAll,
    create,
    update
}