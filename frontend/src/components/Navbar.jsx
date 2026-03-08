import { useState, useEffect } from 'react';
import { Menu, X, Github, Linkedin, Mail } from 'lucide-react';

const Navbar = () => {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => setIsScrolled(window.scrollY > 50);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const navLinks = [
    { name: 'Home', href: '#home' },
    { name: 'About', href: '#about' },
    { name: 'Experience', href: '#experience' },
    { name: 'Skills', href: '#skills' },
    { name: 'Projects', href: '#projects' },
    { name: 'Contact', href: '#contact' },
  ];

  return (
    <nav className={`fixed top-0 left-0 right-0 z-50 transition-all duration-500 ${
      isScrolled 
        ? 'glass bg-slate-900/90 backdrop-blur-xl py-4 shadow-2xl shadow-blue-500/20' 
        : 'bg-transparent py-6'
    }`}>
      <div className="container-custom">
        <div className="flex items-center justify-between">
          {/* Animated Logo */}
          <a href="#home" className="group relative">
            <div className="text-4xl font-black gradient-text transform group-hover:scale-110 transition-transform duration-300">
              BS
            </div>
            <div className="absolute -inset-2 bg-gradient-to-r from-blue-500 to-purple-500 rounded-full blur-lg opacity-0 group-hover:opacity-50 transition-opacity duration-300"></div>
          </a>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-2">
            {navLinks.map((link) => (
              <a
                key={link.name}
                href={link.href}
                className="relative px-4 py-2 text-gray-300 hover:text-white font-medium transition-colors duration-300 group"
              >
                {link.name}
                <span className="absolute inset-0 bg-gradient-to-r from-blue-500/20 to-purple-500/20 rounded-lg opacity-0 group-hover:opacity-100 transition-opacity duration-300 -z-10"></span>
                <span className="absolute bottom-0 left-1/2 w-0 h-0.5 bg-gradient-to-r from-blue-500 to-purple-500 group-hover:w-full group-hover:left-0 transition-all duration-300"></span>
              </a>
            ))}
          </div>

          {/* Social Links */}
          <div className="hidden md:flex items-center space-x-3">
            {[
              { href: 'https://github.com/PhoenixAlgo369', icon: <Github size={20} /> },
              { href: 'https://linkedin.com/in/babajide-salami-', icon: <Linkedin size={20} /> },
              { href: 'mailto:babajide.salami@email.com', icon: <Mail size={20} /> },
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

          {/* Mobile Menu Toggle */}
          <button
            className="md:hidden p-3 glass rounded-xl text-gray-300 hover:text-white transition-all duration-300"
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          >
            {isMobileMenuOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>

        {/* Mobile Menu */}
        {isMobileMenuOpen && (
          <div className="md:hidden mt-6 glass rounded-2xl p-6 animate-fade-in">
            <div className="flex flex-col space-y-4">
              {navLinks.map((link) => (
                <a
                  key={link.name}
                  href={link.href}
                  className="text-gray-300 hover:text-white font-medium py-3 px-4 rounded-xl hover:bg-white/10 transition-all duration-300"
                  onClick={() => setIsMobileMenuOpen(false)}
                >
                  {link.name}
                </a>
              ))}
              <div className="flex items-center space-x-3 pt-4 border-t border-white/10">
                {[Github, Linkedin, Mail].map((Icon, index) => (
                  <a key={index} href="#" className="p-3 glass rounded-xl text-gray-400 hover:text-white hover:bg-white/10 transition-all duration-300">
                    <Icon size={20} />
                  </a>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
