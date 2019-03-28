import React, { useState } from 'react'
import { Form, Button, Message } from 'semantic-ui-react';

import { connect } from 'react-redux'
import { createItem } from '../reducers/itemReducer'

const MarketItemFrom = ({createItem}) => {
    const [name, setName] = useState()
    const [price, setPrice] = useState()
    const [float, setFloat] = useState()
    const [errors, setErrors] = useState({
        name: '',
        price: '',
        float: ''
    })

    const create = () => {
        const fields = validate(name, price, float)
        const disabled = Object.keys(fields).some(f => !fields[f])
        setErrors({
            name: fields['name'] ? '' : name.length < 3 ? 'Name is too short' : 'Name is too long',
            price: fields['price'] ? '' : 'Price cannot be lower than 0',
            float: fields['float'] ? '' : 'Quality value must be between 0 and 1'
        })

        if(!disabled) {
            createItem({name, price, item_float: float})
            setName("")
            setPrice("")
            setFloat("")
        }
    }

    return (
        <Form error={Object.keys(errors).some(e => errors[e] !== '')} onSubmit={() => create()}>
            <Form.Field>
                <label>Name</label>
                <input onChange={(event) => setName(event.target.value)} type='text' placeholder='Name' value={name}/>
            </Form.Field>
            <Form.Field>
                <label>Price</label>
                <input onChange={(event) => setPrice(event.target.value)} type='number' placeholder='Price' value={price}/>
            </Form.Field>
            <Form.Field>
                <label>Quality</label>
                <input onChange={(event) => setFloat(event.target.value)} type='number' placeholder='Quality' value={float} min="0" max="1" step="0.001"/>
            </Form.Field>
            <Button primary type='submit'>Submit</Button>
            <Message error>
                {Object.keys(errors).map(e => <div>{errors[e]}</div>)}
            </Message>
        </Form>
    )
}

const validate = (name, price, float) => {
    return {
        name: name.length > 3 && name.length < 145,
        price: price > 0,
        float: float >= 0 && float <= 1
    }
}

export default connect(null, {createItem})(MarketItemFrom)