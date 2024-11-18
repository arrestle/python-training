import QtQuick 2.15

Rectangle {
    id: blueRect
    width: 75
    height: 50
    color: "blue"
    
    anchors.margins: 10

    Text {
        text: "Blue"
        anchors.centerIn: blueRect
        color: "white"
    }
}