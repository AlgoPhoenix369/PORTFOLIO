import { useState } from 'react';
import { Mail, MapPin, Phone, Send, CheckCircle, AlertCircle, MessageSquare, Sparkles } from 'lucide-react';

const Contact = () => {
  const [formData, setFormData] = useState({ name: '', email: '', subject: '', message: '' });
  const [status, setStatus] = useState({ type: '', message: '' });

  const handleChange = (e) => setFormData({ ...formData, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus({ type: 'success', message: 'Message sent successfully! I\'ll get back to you soon.' });
    setFormData({ name: '', email: '', subject: '', message: '' });
  };

  const contactInfo = [
    { icon: <Mail size={24} />, label: 'Email', value: 'babajide.salami@email.com', gradient: 'from-blue-500 to-cyan-500' },
    { icon: <MapPin size={24} />, label: 'Location', value: 'Croydon, England, UK', gradient: 'from-purple-500 to-pink-500' },
    { icon: <Phone size={24} />, label: 'Phone', value: '+44 7XXX XXXXXX', gradient: 'from-green-500 to-emerald-500' },
  ];

  return (
    <section id="contact" className="section-padding relative overflow-hidden bg-slate-900/50">
      {/* Background */}
      <div className="absolute inset-0 grid-pattern opacity-20"></div>
      <div className="absolute top-0 right-0 w-96 h-96 bg-blue-500/10 rounded-full filter blur-3xl"></div>
      <div className="absolute bottom-0 left-0 w-96 h-96 bg-purple-500/10 rounded-full filter blur-3xl"></div>

      <div className="container-custom relative z-10">
        {/* Section Header */}
        <div className="text-center mb-20">
          <div className="inline-flex items-center space-x-2 glass px-4 py-2 rounded-full mb-6">
            <MessageSquare size={16} className="text-green-400" />
            <span className="text-sm font-medium text-gray-300">Get In Touch</span>
          </div>
          <h2 className="text-5xl md:text-6xl font-black mb-6">
            <span className="gradient-text">Let's Connect</span>
          </h2>
          <p className="text-xl text-gray-400 max-w-3xl mx-auto">
            Have a question or want to work together? I'd love to hear from you!
          </p>
        </div>

        <div className="grid lg:grid-cols-2 gap-12 max-w-7xl mx-auto">
          {/* Contact Info */}
          <div>
            <h3 className="text-3xl font-bold mb-6 text-white">Let's Build Something Amazing</h3>
            <p className="text-gray-300 mb-10 leading-relaxed text-lg">
              I'm currently available for full-time, part-time, contract, and freelance opportunities.
              Whether you have a project in mind or just want to say hello, feel free to reach out!
            </p>

            {/* Contact Cards */}
            <div className="space-y-6 mb-10">
              {contactInfo.map((info, index) => (
                <div key={index} className="group relative">
                  <div className={`absolute -inset-1 bg-gradient-to-r ${info.gradient} rounded-2xl blur opacity-25 group-hover:opacity-75 transition-opacity duration-500`}></div>
                  <div className="relative glass-card p-6 rounded-2xl card-hover flex items-center space-x-5">
                    <div className={`p-4 bg-gradient-to-br ${info.gradient} rounded-xl text-white`}>
                      {info.icon}
                    </div>
                    <div>
                      <h4 className="font-semibold text-gray-400 text-sm mb-1">{info.label}</h4>
                      <p className="text-white font-medium">{info.value}</p>
                    </div>
                  </div>
                </div>
              ))}
            </div>

            {/* Availability */}
            <div className="glass-card p-8 rounded-2xl">
              <div className="flex items-center space-x-3 mb-6">
                <Sparkles size={24} className="text-yellow-400" />
                <h4 className="text-xl font-bold text-white">Availability</h4>
              </div>
              <div className="space-y-4">
                {[
                  { label: 'Location Preference', value: 'Remote (Preferred)', color: 'text-green-400' },
                  { label: 'Work Type', value: 'Full-time, Part-time, Contract', color: 'text-blue-400' },
                  { label: 'Time Zone', value: 'GMT/BST (Flexible)', color: 'text-purple-400' },
                  { label: 'Notice Period', value: 'Available Immediately', color: 'text-pink-400' },
                ].map((item, index) => (
                  <div key={index} className="flex items-center justify-between py-3 border-b border-white/10 last:border-0">
                    <span className="text-gray-400">{item.label}</span>
                    <span className={`font-semibold ${item.color}`}>{item.value}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Contact Form */}
          <div className="relative">
            <div className="absolute -inset-1 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 rounded-3xl blur opacity-30"></div>
            <div className="relative glass-card p-10 rounded-3xl">
              <h3 className="text-2xl font-bold mb-8 text-white">Send a Message</h3>
              
              {status.message && (
                <div className={`mb-8 p-4 rounded-xl flex items-center ${status.type === 'success' ? 'bg-green-500/20 text-green-400' : 'bg-red-500/20 text-red-400'}`}>
                  {status.type === 'success' ? <CheckCircle size={20} className="mr-3" /> : <AlertCircle size={20} className="mr-3" />}
                  {status.message}
                </div>
              )}

              <form onSubmit={handleSubmit} className="space-y-6">
                <div className="grid md:grid-cols-2 gap-6">
                  <div>
                    <label htmlFor="name" className="block font-medium text-gray-300 mb-2">Name</label>
                    <input 
                      id="name" 
                      type="text" 
                      name="name" 
                      value={formData.name} 
                      onChange={handleChange} 
                      required 
                      autoComplete="name"
                      className="w-full px-5 py-4 bg-slate-800/50 border border-white/10 rounded-xl text-white placeholder-gray-500 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300" 
                      placeholder="John Doe" 
                    />
                  </div>
                  <div>
                    <label htmlFor="email" className="block font-medium text-gray-300 mb-2">Email</label>
                    <input 
                      id="email" 
                      type="email" 
                      name="email" 
                      value={formData.email} 
                      onChange={handleChange} 
                      required 
                      autoComplete="email"
                      className="w-full px-5 py-4 bg-slate-800/50 border border-white/10 rounded-xl text-white placeholder-gray-500 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300" 
                      placeholder="john@example.com" 
                    />
                  </div>
                </div>
                <div>
                  <label htmlFor="subject" className="block font-medium text-gray-300 mb-2">Subject</label>
                  <input 
                    id="subject" 
                    type="text" 
                    name="subject" 
                    value={formData.subject} 
                    onChange={handleChange} 
                    required 
                    autoComplete="off"
                    className="w-full px-5 py-4 bg-slate-800/50 border border-white/10 rounded-xl text-white placeholder-gray-500 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300" 
                    placeholder="Project Inquiry" 
                  />
                </div>
                <div>
                  <label htmlFor="message" className="block font-medium text-gray-300 mb-2">Message</label>
                  <textarea 
                    id="message" 
                    name="message" 
                    value={formData.message} 
                    onChange={handleChange} 
                    required 
                    rows={6} 
                    className="w-full px-5 py-4 bg-slate-800/50 border border-white/10 rounded-xl text-white placeholder-gray-500 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-300 resize-none" 
                    placeholder="Tell me about your project..." 
                  />
                </div>
                <button type="submit" className="w-full btn-primary-custom flex items-center justify-center space-x-3">
                  <Send size={20} />
                  <span>Send Message</span>
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Contact;
