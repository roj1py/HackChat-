# HackChat 🔥

A modern TCP-based chat application with a sleek GUI built using Python and CustomTkinter.

## ✨ Features

- **Real-time messaging** - Instant TCP communication
- **Modern GUI** - Clean, dark-themed interface with CustomTkinter
- **Connection management** - Connect/disconnect with status indicators
- **Message history** - Scrollable chat display
- **Keyboard shortcuts** - Ctrl+Enter to send messages quickly
- **Error handling** - Robust connection and error management
- **Multi-threaded** - Separate threads for sending and receiving
- **Clean interface** - Clear chat functionality

## 🚀 Getting Started

### Prerequisites

```bash
pip install customtkinter
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hackchat.git
cd hackchat
```

2. Run the client:
```bash
python HackChat.py
```

## 🎮 Usage

1. **Launch the application** - Run `HackChat.py`
2. **Connect to server** - Click the "Connect" button
3. **Start chatting** - Type your message and click "Send" or press Ctrl+Enter
4. **Disconnect** - Click "Disconnect" when finished

## 🔧 Configuration

The application uses the following default settings:
- **Port**: 8888
- **Server IP**: Auto-detected local IP
- **Buffer Size**: 1024 bytes
- **Encoding**: ASCII

You can modify these settings in the `__init__` method of the `ChatClient` class.

## 📋 Requirements

- Python 3.7+
- CustomTkinter
- Built-in libraries: `socket`, `threading`, `tkinter`

## 🎨 GUI Features

- **Responsive design** - Resizable window with min/max constraints
- **Status indicators** - Real-time connection status
- **Button states** - Context-aware button enabling/disabling
- **Auto-scroll** - Chat automatically scrolls to latest messages
- **System messages** - Clear system notifications and error messages

## 🔮 Future Features

- [ ] Multiple client support
- [ ] File sharing capabilities
- [ ] Encrypted messaging
- [ ] Custom themes
- [ ] Chat rooms
- [ ] User authentication
- [ ] Message timestamps
- [ ] Emoji support

## 🛠️ Technical Details

- **Architecture**: Client-Server TCP model
- **GUI Framework**: CustomTkinter (modern tkinter)
- **Threading**: Separate receive thread for non-blocking GUI
- **Error Handling**: Comprehensive exception handling
- **Memory Management**: Proper socket cleanup on disconnect

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 About

HackChat was created as a learning project to explore TCP networking and modern GUI development in Python. It demonstrates real-time communication, threading, and user interface design principles.

**Built with ❤️ by Roj**

---

⭐ **Star this repository if you found it helpful!**
