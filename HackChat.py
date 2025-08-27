import socket
import threading
import customtkinter
import tkinter.messagebox as messagebox

class ChatClient:
    def __init__(self):
        # Network configuration
        self.port = 8888
        self.server_ip = socket.gethostbyname(socket.gethostname())
        self.server_address = (self.server_ip, self.port)
        self.client = None
        self.header = 1024
        self.format = "ascii"
        self.exit_command = "exit()"
        self.connected = False
        
        # GUI setup
        self.setup_gui()
        
    def setup_gui(self):
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("dark-blue")
        
        self.root = customtkinter.CTk()
        self.root.geometry("800x600")
        self.root.minsize(650, 450)
        self.root.maxsize(1000, 800)
        self.root.title("HackChat Client")
        
        # Main frame
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        # Title
        self.label = customtkinter.CTkLabel(master=self.frame, text="HackChat", font=("Arial", 20))
        self.label.pack(pady=8, padx=10)
        
        # Connection status
        self.status_label = customtkinter.CTkLabel(master=self.frame, text="Status: Disconnected", font=("Arial", 10))
        self.status_label.pack(pady=2)
        
        # Chat display area
        self.chat_box = customtkinter.CTkTextbox(master=self.frame, height=200)
        self.chat_box.pack(pady=5, padx=15, fill="both", expand=True)
        self.chat_box.configure(state="disabled")
        
        # Message input area
        self.senmsg_box = customtkinter.CTkTextbox(master=self.frame, height=50)
        self.senmsg_box.pack(pady=3, padx=15, fill="x")
        
        # Buttons frame
        self.buttons_frame = customtkinter.CTkFrame(master=self.frame, fg_color="transparent")
        self.buttons_frame.pack(pady=5, fill="x")
        
        # Connect button
        self.connect_button = customtkinter.CTkButton(
            master=self.buttons_frame, 
            text="Connect", 
            command=self.connect_to_server,
            width=100,
            height=30
        )
        self.connect_button.pack(side="left", padx=5, expand=True)
        
        # Send button
        self.send_button = customtkinter.CTkButton(
            master=self.buttons_frame, 
            text="Send", 
            command=self.send_message,
            width=100,
            height=30,
            state="disabled"
        )
        self.send_button.pack(side="left", padx=5, expand=True)
        
        # Disconnect button
        self.disconnect_button = customtkinter.CTkButton(
            master=self.buttons_frame, 
            text="Disconnect", 
            command=self.disconnect_from_server,
            width=100,
            height=30,
            state="disabled"
        )
        self.disconnect_button.pack(side="left", padx=5, expand=True)
        
        # Clear chat button
        self.clear_button = customtkinter.CTkButton(
            master=self.buttons_frame, 
            text="Clear Chat", 
            command=self.clear_chat,
            width=100,
            height=30
        )
        self.clear_button.pack(side="left", padx=5, expand=True)
        
        # Bind Enter key to send message
        self.senmsg_box.bind("<Control-Return>", lambda event: self.send_message())
        
        # Handle window closing
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def connect_to_server(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(self.server_address)
            self.connected = True
            
            # Update GUI
            self.update_chat("[SYSTEM] Connected to server successfully!")
            self.status_label.configure(text=f"Status: Connected to {self.server_ip}:{self.port}")
            self.connect_button.configure(state="disabled")
            self.send_button.configure(state="normal")
            self.disconnect_button.configure(state="normal")
            
            # Start receiving thread
            self.recv_thread = threading.Thread(target=self.recv_messages, daemon=True)
            self.recv_thread.start()
            
        except Exception as e:
            messagebox.showerror("Connection Error", f"Failed to connect to server: {str(e)}")
            self.update_chat(f"[ERROR] Connection failed: {str(e)}")
    
    def disconnect_from_server(self):
        try:
            if self.connected and self.client:
                self.connected = False
                self.client.send(self.exit_command.encode(self.format))
                self.client.close()
                
            # Update GUI
            self.update_chat("[SYSTEM] Disconnected from server")
            self.status_label.configure(text="Status: Disconnected")
            self.connect_button.configure(state="normal")
            self.send_button.configure(state="disabled")
            self.disconnect_button.configure(state="disabled")
            
        except Exception as e:
            self.update_chat(f"[ERROR] Disconnect error: {str(e)}")
    
    def send_message(self):
        if not self.connected:
            messagebox.showwarning("Not Connected", "Please connect to server first!")
            return
            
        message = self.senmsg_box.get("1.0", "end-1c").strip()
        
        if message != "":
            try:
                # Send message to server
                self.client.send(message.encode(self.format))
                
                # Display in chat
                self.update_chat(f"You: {message}")
                
                # Clear input box
                self.senmsg_box.delete("1.0", "end")
                
                # Check for exit command
                if message == self.exit_command:
                    self.disconnect_from_server()
                    
            except Exception as e:
                self.update_chat(f"[ERROR] Failed to send message: {str(e)}")
                messagebox.showerror("Send Error", f"Failed to send message: {str(e)}")
    
    def recv_messages(self):
        while self.connected:
            try:
                message = self.client.recv(self.header).decode(self.format).strip()
                if message:
                    # Use root.after to safely update GUI from thread
                    self.root.after(0, lambda msg=message: self.update_chat(f"[MSG] {msg}"))
                else:
                    break
            except Exception as e:
                if self.connected:  # Only show error if we're supposed to be connected
                    self.root.after(0, lambda: self.update_chat(f"[ERROR] Connection lost: {str(e)}"))
                    self.root.after(0, self.disconnect_from_server)
                break
    
    def update_chat(self, message):
        """Safely update the chat display"""
        self.chat_box.configure(state="normal")
        self.chat_box.insert("end", f"{message}\n")
        self.chat_box.configure(state="disabled")
        self.chat_box.see("end")
    
    def clear_chat(self):
        """Clear the chat display"""
        self.chat_box.configure(state="normal")
        self.chat_box.delete("1.0", "end")
        self.chat_box.configure(state="disabled")
    
    def on_closing(self):
        """Handle window closing event"""
        if self.connected:
            self.disconnect_from_server()
        self.root.destroy()
    
    def run(self):
        """Start the application"""
        self.update_chat("[SYSTEM] Welcome to HackChat!")
        self.update_chat("[SYSTEM] Click 'Connect' to join the chat")
        self.update_chat("[SYSTEM] Use Ctrl+Enter to send messages quickly")
        self.root.mainloop()

# Create and run the application
if __name__ == "__main__":
    app = ChatClient()
    app.run()