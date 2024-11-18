import QtQuick 2.15
import "." as Blue

Rectangle {
    id: example7
    width: 200
    height: 200
    color: "green"

    Text {
        id: helloText
        text: "Hello World"
        anchors.centerIn: example7
        color: "white"
        // make the font bigger
        font.pixelSize: 24
    }
    Rectangle {
        id: redRect
        width: 75
        height: 50
        color: "red"
        
        // center the red rectangle below the "Hello World" text
        anchors.top: helloText.bottom
        anchors.horizontalCenter: helloText.horizontalCenter
        anchors.margins: 10

        Text {
            text: "Red"
            anchors.centerIn: redRect
            color: "white"
        }
    }
    // // Embed the blue rectangle from the blue.qml file
    // Blue.blueRect {
    //     id: blueRect
    //     // center the blue rectangle below the red rectangle
    //     anchors.top: redRect.bottom
    //     anchors.horizontalCenter: redRect.horizontalCenter
    // }
}