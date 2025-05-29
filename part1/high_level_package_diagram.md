[DIAGRAM SVG](https://www.mermaidchart.com/raw/87c463eb-cac4-4fea-afac-ae20de9218dc?theme=light&version=v0.1&format=svg)

classDiagram <br>
class PresentationLayer {<br>
    \<\<Interface\>\><br>
    +Login<br>
    +PublishOffer<br>
    +RentPlace<br>
    +UserManagement<br>
}<br>
class BusinessLogicLayer {<br>
    +Client<br>
    +Places<br>
    +Reviews<br>
    +Ammenities<br>
}<br>
class PersistanceLayer {<br>
    +ClientData<br>
    +PlaceData<br>
}<br>
PresentationLayer --> BusinessLogicLayer : Facade Pattern<br>
BusinessLogicLayer --> PersistanceLayer : Database Operation<br>
