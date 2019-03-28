import React, { useState } from 'react'
import { Form, Button } from 'semantic-ui-react';

import { connect } from 'react-redux'
import { createItem } from '../reducers/itemReducer'

const MarketItemFrom = ({createItem}) => {
    const [name, setName] = useState()
    const [price, setPrice] = useState()
    const [float, setFloat] = useState()

    const create = () => {
        createItem({name, price, item_float: float})
        setName("")
        setPrice("")
        setFloat("")
    }

    return (
        <Form onSubmit={() => create()}>
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
        </Form>
    )
}

export default connect(null, {createItem})(MarketItemFrom)