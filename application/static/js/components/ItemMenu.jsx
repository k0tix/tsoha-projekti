import React from 'react'
import { NavLink } from 'react-router-dom'
import { Menu } from 'semantic-ui-react'

const ItemMenu = () => {
    return (
    <Menu inverted>
        <Menu.Item as={NavLink} exact to='/'>Home</Menu.Item>
        <Menu.Item as={NavLink} exact to='/items'>List all items</Menu.Item>
        <Menu.Item as={NavLink} exact to='/items/new'>Add Item</Menu.Item>
    </Menu>
    )
}

export default ItemMenu