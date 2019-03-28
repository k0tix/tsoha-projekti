import React, { useState, useEffect } from 'react'
import { Item, Placeholder, Label, Header, Icon } from 'semantic-ui-react'
import itemService from '../services/itemService'
import PriceForm from './PriceForm';

import { connect } from 'react-redux'

const MarketItems = (props) => {
    return (
        <Item.Group>
            {props.items.map(item => 
                <MarketItem key={item.name} name={item.name} price={item.price} float={item.item_float} id={item.id}/>
            )}
        </Item.Group>
    )
}

const MarketItem = ({name, price, float, id}) => {
    return(
        <div>
            <Item>
                <Item.Content verticalAlign='middle'>
                    <Item.Header>
                        <Header as='h2'>{name}</Header>
                    </Item.Header>
                    <Item.Meta>
                        <Label color='red'>price: {price} €</Label>
                        <Label color='purple'>quality: {float}</Label>
                    </Item.Meta>
                </Item.Content>
                <PriceForm id={id} originalPrice={price}></PriceForm>
            </Item>
        </div>
    )
}

const mapStateToProps = (state) => {
    return {
        items: state.items
    }
}

export default connect(
    mapStateToProps,
    null)(MarketItems)