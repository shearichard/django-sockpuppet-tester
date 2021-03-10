import { Application } from 'stimulus'
import StimulusReflex from 'stimulus_reflex'
import WebsocketConsumer from 'sockpuppet-js'
import TodoaddController from './controllers/todoadd_controller'

const application = Application.start()
const consumer = new WebsocketConsumer(`ws://${window.location.host}/ws/sockpuppet-sync`)

application.register("todoadd", TodoaddController)
StimulusReflex.initialize(application, { consumer })
