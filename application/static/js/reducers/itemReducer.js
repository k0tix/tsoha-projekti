import itemService from '../services/itemService'

const INIT_ITEMS = 'INIT_ITEMS'
const UPDATE_ITEM = 'UPDATE_ITEM'
const CREATE = 'CREATE_ITEM'

const initialState = []

const itemReducer = (state = initialState, action) => {
    switch(action.type) {
        case INIT_ITEMS:
            return action.items
        case CREATE:
            return [...state, action.item]
        case UPDATE_ITEM:
            return state.map(item => item.id !== action.id ? item : Object.assign(item, {price: action.price}))
        default: 
            return state
    }
}

export const itemInitialization = () => {
    return (dispatch) => {
        itemService.getAll().then(items => {
            dispatch({
                type: INIT_ITEMS,
                items
            })
        })
    }
}

export const createItem = (newItem) => {
    return (dispatch) => {
        itemService.create(newItem).then((item) => {
            dispatch({
                type: CREATE,
                item
            })
        })
    }
}

export const updateItem = (id, price) => {
    return (dispatch) => {
        itemService.update(id, price).then(() => {
            dispatch({
                type: UPDATE_ITEM,
                id,
                price
            })
        })
    }
}

export default itemReducer