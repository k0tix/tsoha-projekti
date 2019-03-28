import React, { Component } from 'react'
import { Header, Button, Item, Grid, Segment} from 'semantic-ui-react'
import { BrowserRouter as Router, Route, Link } from 'react-router-dom'

import MarketItems from './components/MarketItems'
import ItemMenu from './components/ItemMenu'
import MarketItemForm from './components/MarketItemForm'

import { connect } from 'react-redux'

import { itemInitialization } from './reducers/itemReducer'


class App extends Component {

    componentDidMount() {
        this.props.itemInitialization()
    }

    render() {
        return (
            <div>
                <Router>
                    {/*<Button onClick={() => console.log("MOI")}>List all items</Button>
                    <Button>Add new item</Button>*/}
                    <Grid>
                        <Grid.Row>
                            <Grid.Column>
                                <Header as='h1' style={{ margin: '1em 0em', textAlign: 'center'}}>Byteskins</Header>
                            </Grid.Column>
                        </Grid.Row>
                        <Grid.Row>
                            <Grid.Column>
                                <ItemMenu></ItemMenu>
                            </Grid.Column>
                        </Grid.Row>
                        <Grid.Row>
                            <Grid.Column>
                                <Segment>
                                    <Route exact path='/' render={() => <Header as='h2'>Welcome to Byteskins - A marketplace for in-game items</Header>}/>
                                    <Route exact path='/items' render={() => <MarketItems></MarketItems>} />
                                    <Route exact path='/items/new' render={() => <MarketItemForm></MarketItemForm>} />
                                </Segment>
                            </Grid.Column>
                        </Grid.Row>
                    </Grid>
                </Router>
            </div>
        )
    }
}

export default connect(null, {itemInitialization})(App)