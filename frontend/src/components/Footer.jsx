import { Github, Linkedin, Mail, Heart, Rocket } from 'lucide-react';

const Footer = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="relative overflow-hidden bg-slate-900 border-t border-white/10">
      {/* Background */}
      <div className="absolute inset-0 dot-pattern opacity-10"></div>
      <div className="absolute top-0 left-1/2 w-96 h-96 bg-blue-500/10 rounded-full filter blur-3xl transform -translate-x-1/2"></div>

      <div className="container-custom relative z-10 py-16">
        <div className="grid md:grid-cols-4 gap-12 mb-12">
          {/* Brand */}
          <div className="md:col-span-2">
            <a href="#home" className="inline-block text-4xl font-black gradient-text mb-6">BS</a>
            <p className="text-gray-400 leading-relaxed mb-6 max-w-md">
              AI Training Specialist & Software Engineer passionate about advancing AI through 
              quality training data and responsible AI practices. Building the future of intelligent systems.
            </p>
            <div className="flex items-center space-x-4">
              {[
                { href: 'https://github.com/PhoenixAlgo369', icon: <Github size={22} /> },
                { href: 'https://linkedin.com/in/babajide-salami-', icon: <Linkedin size={22} /> },
                { href: 'mailto:babajide.salami@email.com', icon: <Mail size={22} /> },
              ].map((social, index) => (
                <a
                  key={index}
                  href={social.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="p-3 glass rounded-xl text-gray-400 hover:text-white hover:bg-white/10 transition-all duration-300 hover:scale-110"
                >
                  {social.icon}
                </a>
              ))}
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="text-lg font-bold text-white mb-6 flex items-center">
              <Rocket size={20} className="mr-2 text-blue-400" />
              Quick Links
            </h4>
            <ul className="space-y-3">
              {['Home', 'About', 'Experience', 'Skills', 'Projects', 'Contact'].map((item) => (
                <li key={item}>
                  <a href={`#${item.toLowerCase()}`} className="text-gray-400 hover:text-white transition-colors duration-300 flex items-center group">
                    <span className="w-0 h-0.5 bg-gradient-to-r from-blue-500 to-purple-500 group-hover:w-6 transition-all duration-300 mr-0 group-hover:mr-2"></span>
                    {item}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Contact */}
          <div>
            <h4 className="text-lg font-bold text-white mb-6">Get In Touch</h4>
            <div className="space-y-4">
              <div className="flex items-center space-x-3 text-gray-400 hover:text-white transition-colors duration-300">
                <Mail size={18} className="text-blue-400" />
                <span className="text-sm">babajide.salami@email.com</span>
              </div>
              <div className="flex items-center space-x-3 text-gray-400 hover:text-white transition-colors duration-300">
                <MapPin size={18} className="text-purple-400" />
                <span className="text-sm">Croydon, England, UK</span>
              </div>
              <div className="pt-4">
                <div className="inline-flex items-center space-x-2 px-4 py-2 bg-green-500/20 rounded-full">
                  <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
                  <span className="text-green-400 text-sm font-medium">Available for work</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="pt-8 border-t border-white/10">
          <div className="flex flex-col md:flex-row items-center justify-between gap-4">
            <p className="text-gray-500 text-sm text-center md:text-left">
              © {currentYear} Babajide Salami. All rights reserved.
            </p>
            <p className="text-gray-500 text-sm flex items-center">
              Made with <Heart size={16} className="mx-2 text-red-500 animate-pulse" /> using React & Tailwind CSS
            </p>
            <a href="#home" className="text-gray-500 hover:text-white text-sm transition-colors duration-300">
              Back to Top ↑
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
};

// Import MapPin
import { MapPin } from 'lucide-react';

export default Footer;
