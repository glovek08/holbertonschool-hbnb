[DIAGRAM SVG](https://www.mermaidchart.com/raw/87c463eb-cac4-4fea-afac-ae20de9218dc?theme=light&version=v0.1&format=svg)

classDiagram
class PresentationLayer {
    <<Interface>>
    +Login
    +PublishOffer
    +RentPlace
    +UserManagement
}
class BusinessLogicLayer {
    +Client
    +Places
    +Reviews
    +Ammenities
}
class PersistanceLayer {
    +ClientData
    +PlaceData
}
PresentationLayer --> BusinessLogicLayer : Facade Pattern
BusinessLogicLayer --> PersistanceLayer : Database Operation