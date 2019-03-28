import React, { useState } from 'react'
import { Form, Button } from 'semantic-ui-react'

import { connect } from 'react-redux'
import { updateItem } from '../reducers/itemReducer'

const PriceForm = ({id, originalPrice, updateItem}) => {
    const [price, setPrice] = useState(originalPrice)

    return (
        <div style={{margin: '1em'}}>
            <Form size='small' onSubmit={() => updateItem(id, price)}>
                <Form.Field>
                    <label>Change price</label>
                    <input onChange={(event) => setPrice(event.target.value)} type='number' placeholder='New price' value={price}/>
                </Form.Field>
                <Button primary type='submit'>Submit</Button>
            </Form>
        </div>
    )
}

export default connect(null, {updateItem})(PriceForm)