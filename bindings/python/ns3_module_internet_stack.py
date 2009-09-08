from pybindgen import Module, FileCodeSink, param, retval, cppclass, typehandlers

def register_types(module):
    root_module = module.get_root()
    
    ## icmpv4.h: ns3::Icmpv4DestinationUnreachable [class]
    module.add_class('Icmpv4DestinationUnreachable', parent=root_module['ns3::Header'])
    ## icmpv4.h: ns3::Icmpv4DestinationUnreachable [enumeration]
    module.add_enum('', ['NET_UNREACHABLE', 'HOST_UNREACHABLE', 'PROTOCOL_UNREACHABLE', 'PORT_UNREACHABLE', 'FRAG_NEEDED', 'SOURCE_ROUTE_FAILED'], outer_class=root_module['ns3::Icmpv4DestinationUnreachable'])
    ## icmpv4.h: ns3::Icmpv4Echo [class]
    module.add_class('Icmpv4Echo', parent=root_module['ns3::Header'])
    ## icmpv4.h: ns3::Icmpv4Header [class]
    module.add_class('Icmpv4Header', parent=root_module['ns3::Header'])
    ## icmpv4.h: ns3::Icmpv4Header [enumeration]
    module.add_enum('', ['ECHO_REPLY', 'DEST_UNREACH', 'ECHO', 'TIME_EXCEEDED'], outer_class=root_module['ns3::Icmpv4Header'])
    ## icmpv4.h: ns3::Icmpv4TimeExceeded [class]
    module.add_class('Icmpv4TimeExceeded', parent=root_module['ns3::Header'])
    ## icmpv4.h: ns3::Icmpv4TimeExceeded [enumeration]
    module.add_enum('', ['TIME_TO_LIVE', 'FRAGMENT_REASSEMBLY'], outer_class=root_module['ns3::Icmpv4TimeExceeded'])
    ## icmpv6-header.h: ns3::Icmpv6Header [class]
    module.add_class('Icmpv6Header', parent=root_module['ns3::Header'])
    ## icmpv6-header.h: ns3::Icmpv6Header::Type_e [enumeration]
    module.add_enum('Type_e', ['ICMPV6_ERROR_DESTINATION_UNREACHABLE', 'ICMPV6_ERROR_PACKET_TOO_BIG', 'ICMPV6_ERROR_TIME_EXCEEDED', 'ICMPV6_ERROR_PARAMETER_ERROR', 'ICMPV6_ECHO_REQUEST', 'ICMPV6_ECHO_REPLY', 'ICMPV6_SUBSCRIBE_REQUEST', 'ICMPV6_SUBSCRIBE_REPORT', 'ICMPV6_SUBSCRIVE_END', 'ICMPV6_ND_ROUTER_SOLICITATION', 'ICMPV6_ND_ROUTER_ADVERTISEMENT', 'ICMPV6_ND_NEIGHBOR_SOLICITATION', 'ICMPV6_ND_NEIGHBOR_ADVERTISEMENT', 'ICMPV6_ND_REDIRECTION', 'ICMPV6_ROUTER_RENUMBER', 'ICMPV6_INFORMATION_REQUEST', 'ICMPV6_INFORMATION_RESPONSE', 'ICMPV6_INVERSE_ND_SOLICITATION', 'ICMPV6_INVERSE_ND_ADVERSTISEMENT', 'ICMPV6_MLDV2_SUBSCRIBE_REPORT', 'ICMPV6_MOBILITY_HA_DISCOVER_REQUEST', 'ICMPV6_MOBILITY_HA_DISCOVER_RESPONSE', 'ICMPV6_MOBILITY_MOBILE_PREFIX_SOLICITATION', 'ICMPV6_SECURE_ND_CERTIFICATE_PATH_SOLICITATION', 'ICMPV6_SECURE_ND_CERTIFICATE_PATH_ADVERTISEMENT', 'ICMPV6_EXPERIMENTAL_MOBILITY'], outer_class=root_module['ns3::Icmpv6Header'])
    ## icmpv6-header.h: ns3::Icmpv6Header::OptionType_e [enumeration]
    module.add_enum('OptionType_e', ['ICMPV6_OPT_LINK_LAYER_SOURCE', 'ICMPV6_OPT_LINK_LAYER_TARGET', 'ICMPV6_OPT_PREFIX', 'ICMPV6_OPT_REDIRECTED', 'ICMPV6_OPT_MTU'], outer_class=root_module['ns3::Icmpv6Header'])
    ## icmpv6-header.h: ns3::Icmpv6Header::ErrorDestinationUnreachable_e [enumeration]
    module.add_enum('ErrorDestinationUnreachable_e', ['ICMPV6_NO_ROUTE', 'ICMPV6_ADM_PROHIBITED', 'ICMPV6_NOT_NEIGHBOUR', 'ICMPV6_ADDR_UNREACHABLE', 'ICMPV6_PORT_UNREACHABLE'], outer_class=root_module['ns3::Icmpv6Header'])
    ## icmpv6-header.h: ns3::Icmpv6Header::ErrorTimeExceeded_e [enumeration]
    module.add_enum('ErrorTimeExceeded_e', ['ICMPV6_HOPLIMIT', 'ICMPV6_FRAGTIME'], outer_class=root_module['ns3::Icmpv6Header'])
    ## icmpv6-header.h: ns3::Icmpv6Header::ErrorParameterError_e [enumeration]
    module.add_enum('ErrorParameterError_e', ['ICMPV6_MALFORMED_HEADER', 'ICMPV6_UNKNOWN_NEXT_HEADER', 'ICMPV6_UNKNOWN_OPTION'], outer_class=root_module['ns3::Icmpv6Header'])
    ## icmpv6-header.h: ns3::Icmpv6NA [class]
    module.add_class('Icmpv6NA', parent=root_module['ns3::Icmpv6Header'])
    ## icmpv6-header.h: ns3::Icmpv6NS [class]
    module.add_class('Icmpv6NS', parent=root_module['ns3::Icmpv6Header'])
    ## icmpv6-header.h: ns3::Icmpv6OptionHeader [class]
    module.add_class('Icmpv6OptionHeader', parent=root_module['ns3::Header'])
    ## icmpv6-header.h: ns3::Icmpv6OptionLinkLayerAddress [class]
    module.add_class('Icmpv6OptionLinkLayerAddress', parent=root_module['ns3::Icmpv6OptionHeader'])
    ## icmpv6-header.h: ns3::Icmpv6OptionMtu [class]
    module.add_class('Icmpv6OptionMtu', parent=root_module['ns3::Icmpv6OptionHeader'])
    ## icmpv6-header.h: ns3::Icmpv6OptionPrefixInformation [class]
    module.add_class('Icmpv6OptionPrefixInformation', parent=root_module['ns3::Icmpv6OptionHeader'])
    ## icmpv6-header.h: ns3::Icmpv6OptionRedirected [class]
    module.add_class('Icmpv6OptionRedirected', parent=root_module['ns3::Icmpv6OptionHeader'])
    ## icmpv6-header.h: ns3::Icmpv6ParameterError [class]
    module.add_class('Icmpv6ParameterError', parent=root_module['ns3::Icmpv6Header'])
    ## icmpv6-header.h: ns3::Icmpv6RA [class]
    module.add_class('Icmpv6RA', parent=root_module['ns3::Icmpv6Header'])
    ## icmpv6-header.h: ns3::Icmpv6RS [class]
    module.add_class('Icmpv6RS', parent=root_module['ns3::Icmpv6Header'])
    ## icmpv6-header.h: ns3::Icmpv6Redirection [class]
    module.add_class('Icmpv6Redirection', parent=root_module['ns3::Icmpv6Header'])
    ## icmpv6-header.h: ns3::Icmpv6TimeExceeded [class]
    module.add_class('Icmpv6TimeExceeded', parent=root_module['ns3::Icmpv6Header'])
    ## icmpv6-header.h: ns3::Icmpv6TooBig [class]
    module.add_class('Icmpv6TooBig', parent=root_module['ns3::Icmpv6Header'])
    ## tcp-header.h: ns3::TcpHeader [class]
    module.add_class('TcpHeader', parent=root_module['ns3::Header'])
    ## tcp-header.h: ns3::TcpHeader::Flags_t [enumeration]
    module.add_enum('Flags_t', ['NONE', 'FIN', 'SYN', 'RST', 'PSH', 'ACK', 'URG'], outer_class=root_module['ns3::TcpHeader'])
    ## udp-header.h: ns3::UdpHeader [class]
    module.add_class('UdpHeader', parent=root_module['ns3::Header'])
    ## arp-cache.h: ns3::ArpCache [class]
    module.add_class('ArpCache', parent=root_module['ns3::Object'])
    ## arp-cache.h: ns3::ArpCache::Entry [class]
    module.add_class('Entry', outer_class=root_module['ns3::ArpCache'])
    ## arp-l3-protocol.h: ns3::ArpL3Protocol [class]
    module.add_class('ArpL3Protocol', parent=root_module['ns3::Object'])
    ## icmpv6-header.h: ns3::Icmpv6DestinationUnreachable [class]
    module.add_class('Icmpv6DestinationUnreachable', parent=root_module['ns3::Icmpv6Header'])
    ## icmpv6-header.h: ns3::Icmpv6Echo [class]
    module.add_class('Icmpv6Echo', parent=root_module['ns3::Icmpv6Header'])
    ## ipv4-l3-protocol.h: ns3::Ipv4L3Protocol [class]
    module.add_class('Ipv4L3Protocol', parent=root_module['ns3::Ipv4'])
    ## ipv4-l4-protocol.h: ns3::Ipv4L4Protocol [class]
    module.add_class('Ipv4L4Protocol', parent=root_module['ns3::Object'])
    ## ipv4-l4-protocol.h: ns3::Ipv4L4Protocol::RxStatus [enumeration]
    module.add_enum('RxStatus', ['RX_OK', 'RX_CSUM_FAILED', 'RX_ENDPOINT_UNREACH'], outer_class=root_module['ns3::Ipv4L4Protocol'])
    ## tcp-l4-protocol.h: ns3::TcpL4Protocol [class]
    module.add_class('TcpL4Protocol', parent=root_module['ns3::Ipv4L4Protocol'])
    ## udp-l4-protocol.h: ns3::UdpL4Protocol [class]
    module.add_class('UdpL4Protocol', parent=root_module['ns3::Ipv4L4Protocol'])
    ## icmpv4-l4-protocol.h: ns3::Icmpv4L4Protocol [class]
    module.add_class('Icmpv4L4Protocol', parent=root_module['ns3::Ipv4L4Protocol'])
    
    ## Register a nested module for the namespace Config
    
    nested_module = module.add_cpp_namespace('Config')
    register_types_ns3_Config(nested_module)
    
    
    ## Register a nested module for the namespace TimeStepPrecision
    
    nested_module = module.add_cpp_namespace('TimeStepPrecision')
    register_types_ns3_TimeStepPrecision(nested_module)
    
    
    ## Register a nested module for the namespace addressUtils
    
    nested_module = module.add_cpp_namespace('addressUtils')
    register_types_ns3_addressUtils(nested_module)
    
    
    ## Register a nested module for the namespace internal
    
    nested_module = module.add_cpp_namespace('internal')
    register_types_ns3_internal(nested_module)
    
    
    ## Register a nested module for the namespace olsr
    
    nested_module = module.add_cpp_namespace('olsr')
    register_types_ns3_olsr(nested_module)
    

def register_types_ns3_Config(module):
    root_module = module.get_root()
    

def register_types_ns3_TimeStepPrecision(module):
    root_module = module.get_root()
    

def register_types_ns3_addressUtils(module):
    root_module = module.get_root()
    

def register_types_ns3_internal(module):
    root_module = module.get_root()
    

def register_types_ns3_olsr(module):
    root_module = module.get_root()
    

def register_methods(root_module):
    register_Ns3Icmpv4DestinationUnreachable_methods(root_module, root_module['ns3::Icmpv4DestinationUnreachable'])
    register_Ns3Icmpv4Echo_methods(root_module, root_module['ns3::Icmpv4Echo'])
    register_Ns3Icmpv4Header_methods(root_module, root_module['ns3::Icmpv4Header'])
    register_Ns3Icmpv4TimeExceeded_methods(root_module, root_module['ns3::Icmpv4TimeExceeded'])
    register_Ns3Icmpv6Header_methods(root_module, root_module['ns3::Icmpv6Header'])
    register_Ns3Icmpv6NA_methods(root_module, root_module['ns3::Icmpv6NA'])
    register_Ns3Icmpv6NS_methods(root_module, root_module['ns3::Icmpv6NS'])
    register_Ns3Icmpv6OptionHeader_methods(root_module, root_module['ns3::Icmpv6OptionHeader'])
    register_Ns3Icmpv6OptionLinkLayerAddress_methods(root_module, root_module['ns3::Icmpv6OptionLinkLayerAddress'])
    register_Ns3Icmpv6OptionMtu_methods(root_module, root_module['ns3::Icmpv6OptionMtu'])
    register_Ns3Icmpv6OptionPrefixInformation_methods(root_module, root_module['ns3::Icmpv6OptionPrefixInformation'])
    register_Ns3Icmpv6OptionRedirected_methods(root_module, root_module['ns3::Icmpv6OptionRedirected'])
    register_Ns3Icmpv6ParameterError_methods(root_module, root_module['ns3::Icmpv6ParameterError'])
    register_Ns3Icmpv6RA_methods(root_module, root_module['ns3::Icmpv6RA'])
    register_Ns3Icmpv6RS_methods(root_module, root_module['ns3::Icmpv6RS'])
    register_Ns3Icmpv6Redirection_methods(root_module, root_module['ns3::Icmpv6Redirection'])
    register_Ns3Icmpv6TimeExceeded_methods(root_module, root_module['ns3::Icmpv6TimeExceeded'])
    register_Ns3Icmpv6TooBig_methods(root_module, root_module['ns3::Icmpv6TooBig'])
    register_Ns3TcpHeader_methods(root_module, root_module['ns3::TcpHeader'])
    register_Ns3UdpHeader_methods(root_module, root_module['ns3::UdpHeader'])
    register_Ns3ArpCache_methods(root_module, root_module['ns3::ArpCache'])
    register_Ns3ArpCacheEntry_methods(root_module, root_module['ns3::ArpCache::Entry'])
    register_Ns3ArpL3Protocol_methods(root_module, root_module['ns3::ArpL3Protocol'])
    register_Ns3Icmpv6DestinationUnreachable_methods(root_module, root_module['ns3::Icmpv6DestinationUnreachable'])
    register_Ns3Icmpv6Echo_methods(root_module, root_module['ns3::Icmpv6Echo'])
    register_Ns3Ipv4L3Protocol_methods(root_module, root_module['ns3::Ipv4L3Protocol'])
    register_Ns3Ipv4L4Protocol_methods(root_module, root_module['ns3::Ipv4L4Protocol'])
    register_Ns3TcpL4Protocol_methods(root_module, root_module['ns3::TcpL4Protocol'])
    register_Ns3UdpL4Protocol_methods(root_module, root_module['ns3::UdpL4Protocol'])
    register_Ns3Icmpv4L4Protocol_methods(root_module, root_module['ns3::Icmpv4L4Protocol'])
    return

def register_Ns3Icmpv4DestinationUnreachable_methods(root_module, cls):
    ## icmpv4.h: ns3::Icmpv4DestinationUnreachable::Icmpv4DestinationUnreachable(ns3::Icmpv4DestinationUnreachable const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv4DestinationUnreachable const &', 'arg0')])
    ## icmpv4.h: ns3::Icmpv4DestinationUnreachable::Icmpv4DestinationUnreachable() [constructor]
    cls.add_constructor([])
    ## icmpv4.h: void ns3::Icmpv4DestinationUnreachable::GetData(uint8_t * payload) const [member function]
    cls.add_method('GetData', 
                   'void', 
                   [param('uint8_t *', 'payload')], 
                   is_const=True)
    ## icmpv4.h: ns3::Ipv4Header ns3::Icmpv4DestinationUnreachable::GetHeader() const [member function]
    cls.add_method('GetHeader', 
                   'ns3::Ipv4Header', 
                   [], 
                   is_const=True)
    ## icmpv4.h: uint16_t ns3::Icmpv4DestinationUnreachable::GetNextHopMtu() const [member function]
    cls.add_method('GetNextHopMtu', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## icmpv4.h: static ns3::TypeId ns3::Icmpv4DestinationUnreachable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv4.h: void ns3::Icmpv4DestinationUnreachable::SetData(ns3::Ptr<ns3::Packet const> data) [member function]
    cls.add_method('SetData', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'data')])
    ## icmpv4.h: void ns3::Icmpv4DestinationUnreachable::SetHeader(ns3::Ipv4Header header) [member function]
    cls.add_method('SetHeader', 
                   'void', 
                   [param('ns3::Ipv4Header', 'header')])
    ## icmpv4.h: void ns3::Icmpv4DestinationUnreachable::SetNextHopMtu(uint16_t mtu) [member function]
    cls.add_method('SetNextHopMtu', 
                   'void', 
                   [param('uint16_t', 'mtu')])
    ## icmpv4.h: uint32_t ns3::Icmpv4DestinationUnreachable::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   visibility='private', is_virtual=True)
    ## icmpv4.h: ns3::TypeId ns3::Icmpv4DestinationUnreachable::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    ## icmpv4.h: uint32_t ns3::Icmpv4DestinationUnreachable::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    ## icmpv4.h: void ns3::Icmpv4DestinationUnreachable::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, visibility='private', is_virtual=True)
    ## icmpv4.h: void ns3::Icmpv4DestinationUnreachable::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3Icmpv4Echo_methods(root_module, cls):
    ## icmpv4.h: ns3::Icmpv4Echo::Icmpv4Echo(ns3::Icmpv4Echo const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv4Echo const &', 'arg0')])
    ## icmpv4.h: ns3::Icmpv4Echo::Icmpv4Echo() [constructor]
    cls.add_constructor([])
    ## icmpv4.h: uint32_t ns3::Icmpv4Echo::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv4.h: uint32_t ns3::Icmpv4Echo::GetData(uint8_t * payload) const [member function]
    cls.add_method('GetData', 
                   'uint32_t', 
                   [param('uint8_t *', 'payload')], 
                   is_const=True)
    ## icmpv4.h: uint32_t ns3::Icmpv4Echo::GetDataSize() const [member function]
    cls.add_method('GetDataSize', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## icmpv4.h: uint16_t ns3::Icmpv4Echo::GetIdentifier() const [member function]
    cls.add_method('GetIdentifier', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## icmpv4.h: ns3::TypeId ns3::Icmpv4Echo::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv4.h: uint16_t ns3::Icmpv4Echo::GetSequenceNumber() const [member function]
    cls.add_method('GetSequenceNumber', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## icmpv4.h: uint32_t ns3::Icmpv4Echo::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv4.h: static ns3::TypeId ns3::Icmpv4Echo::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv4.h: void ns3::Icmpv4Echo::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## icmpv4.h: void ns3::Icmpv4Echo::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv4.h: void ns3::Icmpv4Echo::SetData(ns3::Ptr<ns3::Packet const> data) [member function]
    cls.add_method('SetData', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'data')])
    ## icmpv4.h: void ns3::Icmpv4Echo::SetIdentifier(uint16_t id) [member function]
    cls.add_method('SetIdentifier', 
                   'void', 
                   [param('uint16_t', 'id')])
    ## icmpv4.h: void ns3::Icmpv4Echo::SetSequenceNumber(uint16_t seq) [member function]
    cls.add_method('SetSequenceNumber', 
                   'void', 
                   [param('uint16_t', 'seq')])
    return

def register_Ns3Icmpv4Header_methods(root_module, cls):
    ## icmpv4.h: ns3::Icmpv4Header::Icmpv4Header(ns3::Icmpv4Header const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv4Header const &', 'arg0')])
    ## icmpv4.h: ns3::Icmpv4Header::Icmpv4Header() [constructor]
    cls.add_constructor([])
    ## icmpv4.h: uint32_t ns3::Icmpv4Header::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv4.h: void ns3::Icmpv4Header::EnableChecksum() [member function]
    cls.add_method('EnableChecksum', 
                   'void', 
                   [])
    ## icmpv4.h: uint8_t ns3::Icmpv4Header::GetCode() const [member function]
    cls.add_method('GetCode', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## icmpv4.h: ns3::TypeId ns3::Icmpv4Header::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv4.h: uint32_t ns3::Icmpv4Header::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv4.h: uint8_t ns3::Icmpv4Header::GetType() const [member function]
    cls.add_method('GetType', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## icmpv4.h: static ns3::TypeId ns3::Icmpv4Header::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv4.h: void ns3::Icmpv4Header::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## icmpv4.h: void ns3::Icmpv4Header::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv4.h: void ns3::Icmpv4Header::SetCode(uint8_t code) [member function]
    cls.add_method('SetCode', 
                   'void', 
                   [param('uint8_t', 'code')])
    ## icmpv4.h: void ns3::Icmpv4Header::SetType(uint8_t type) [member function]
    cls.add_method('SetType', 
                   'void', 
                   [param('uint8_t', 'type')])
    return

def register_Ns3Icmpv4TimeExceeded_methods(root_module, cls):
    ## icmpv4.h: ns3::Icmpv4TimeExceeded::Icmpv4TimeExceeded(ns3::Icmpv4TimeExceeded const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv4TimeExceeded const &', 'arg0')])
    ## icmpv4.h: ns3::Icmpv4TimeExceeded::Icmpv4TimeExceeded() [constructor]
    cls.add_constructor([])
    ## icmpv4.h: uint32_t ns3::Icmpv4TimeExceeded::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv4.h: void ns3::Icmpv4TimeExceeded::GetData(uint8_t * payload) const [member function]
    cls.add_method('GetData', 
                   'void', 
                   [param('uint8_t *', 'payload')], 
                   is_const=True)
    ## icmpv4.h: ns3::Ipv4Header ns3::Icmpv4TimeExceeded::GetHeader() const [member function]
    cls.add_method('GetHeader', 
                   'ns3::Ipv4Header', 
                   [], 
                   is_const=True)
    ## icmpv4.h: ns3::TypeId ns3::Icmpv4TimeExceeded::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv4.h: uint32_t ns3::Icmpv4TimeExceeded::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv4.h: static ns3::TypeId ns3::Icmpv4TimeExceeded::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv4.h: void ns3::Icmpv4TimeExceeded::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## icmpv4.h: void ns3::Icmpv4TimeExceeded::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv4.h: void ns3::Icmpv4TimeExceeded::SetData(ns3::Ptr<ns3::Packet const> data) [member function]
    cls.add_method('SetData', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet const >', 'data')])
    ## icmpv4.h: void ns3::Icmpv4TimeExceeded::SetHeader(ns3::Ipv4Header header) [member function]
    cls.add_method('SetHeader', 
                   'void', 
                   [param('ns3::Ipv4Header', 'header')])
    return

def register_Ns3Icmpv6Header_methods(root_module, cls):
    ## icmpv6-header.h: ns3::Icmpv6Header::Icmpv6Header(ns3::Icmpv6Header const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv6Header const &', 'arg0')])
    ## icmpv6-header.h: ns3::Icmpv6Header::Icmpv6Header() [constructor]
    cls.add_constructor([])
    ## icmpv6-header.h: void ns3::Icmpv6Header::CalculatePseudoHeaderChecksum(ns3::Ipv6Address src, ns3::Ipv6Address dst, uint16_t length, uint8_t protocol) [member function]
    cls.add_method('CalculatePseudoHeaderChecksum', 
                   'void', 
                   [param('ns3::Ipv6Address', 'src'), param('ns3::Ipv6Address', 'dst'), param('uint16_t', 'length'), param('uint8_t', 'protocol')])
    ## icmpv6-header.h: uint32_t ns3::Icmpv6Header::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv6-header.h: uint16_t ns3::Icmpv6Header::GetChecksum() const [member function]
    cls.add_method('GetChecksum', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint8_t ns3::Icmpv6Header::GetCode() const [member function]
    cls.add_method('GetCode', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: ns3::TypeId ns3::Icmpv6Header::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6Header::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: uint8_t ns3::Icmpv6Header::GetType() const [member function]
    cls.add_method('GetType', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: static ns3::TypeId ns3::Icmpv6Header::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv6-header.h: void ns3::Icmpv6Header::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6Header::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6Header::SetChecksum(uint16_t checksum) [member function]
    cls.add_method('SetChecksum', 
                   'void', 
                   [param('uint16_t', 'checksum')])
    ## icmpv6-header.h: void ns3::Icmpv6Header::SetCode(uint8_t code) [member function]
    cls.add_method('SetCode', 
                   'void', 
                   [param('uint8_t', 'code')])
    ## icmpv6-header.h: void ns3::Icmpv6Header::SetType(uint8_t type) [member function]
    cls.add_method('SetType', 
                   'void', 
                   [param('uint8_t', 'type')])
    return

def register_Ns3Icmpv6NA_methods(root_module, cls):
    ## icmpv6-header.h: ns3::Icmpv6NA::Icmpv6NA(ns3::Icmpv6NA const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv6NA const &', 'arg0')])
    ## icmpv6-header.h: ns3::Icmpv6NA::Icmpv6NA() [constructor]
    cls.add_constructor([])
    ## icmpv6-header.h: uint32_t ns3::Icmpv6NA::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv6-header.h: bool ns3::Icmpv6NA::GetFlagO() const [member function]
    cls.add_method('GetFlagO', 
                   'bool', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: bool ns3::Icmpv6NA::GetFlagR() const [member function]
    cls.add_method('GetFlagR', 
                   'bool', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: bool ns3::Icmpv6NA::GetFlagS() const [member function]
    cls.add_method('GetFlagS', 
                   'bool', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: ns3::TypeId ns3::Icmpv6NA::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: ns3::Ipv6Address ns3::Icmpv6NA::GetIpv6Target() const [member function]
    cls.add_method('GetIpv6Target', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6NA::GetReserved() const [member function]
    cls.add_method('GetReserved', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6NA::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: static ns3::TypeId ns3::Icmpv6NA::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv6-header.h: void ns3::Icmpv6NA::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6NA::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6NA::SetFlagO(bool o) [member function]
    cls.add_method('SetFlagO', 
                   'void', 
                   [param('bool', 'o')])
    ## icmpv6-header.h: void ns3::Icmpv6NA::SetFlagR(bool r) [member function]
    cls.add_method('SetFlagR', 
                   'void', 
                   [param('bool', 'r')])
    ## icmpv6-header.h: void ns3::Icmpv6NA::SetFlagS(bool s) [member function]
    cls.add_method('SetFlagS', 
                   'void', 
                   [param('bool', 's')])
    ## icmpv6-header.h: void ns3::Icmpv6NA::SetIpv6Target(ns3::Ipv6Address target) [member function]
    cls.add_method('SetIpv6Target', 
                   'void', 
                   [param('ns3::Ipv6Address', 'target')])
    ## icmpv6-header.h: void ns3::Icmpv6NA::SetReserved(uint32_t reserved) [member function]
    cls.add_method('SetReserved', 
                   'void', 
                   [param('uint32_t', 'reserved')])
    return

def register_Ns3Icmpv6NS_methods(root_module, cls):
    ## icmpv6-header.h: ns3::Icmpv6NS::Icmpv6NS(ns3::Icmpv6NS const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv6NS const &', 'arg0')])
    ## icmpv6-header.h: ns3::Icmpv6NS::Icmpv6NS(ns3::Ipv6Address target) [constructor]
    cls.add_constructor([param('ns3::Ipv6Address', 'target')])
    ## icmpv6-header.h: ns3::Icmpv6NS::Icmpv6NS() [constructor]
    cls.add_constructor([])
    ## icmpv6-header.h: uint32_t ns3::Icmpv6NS::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv6-header.h: ns3::TypeId ns3::Icmpv6NS::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: ns3::Ipv6Address ns3::Icmpv6NS::GetIpv6Target() const [member function]
    cls.add_method('GetIpv6Target', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6NS::GetReserved() const [member function]
    cls.add_method('GetReserved', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6NS::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: static ns3::TypeId ns3::Icmpv6NS::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv6-header.h: void ns3::Icmpv6NS::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6NS::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6NS::SetIpv6Target(ns3::Ipv6Address target) [member function]
    cls.add_method('SetIpv6Target', 
                   'void', 
                   [param('ns3::Ipv6Address', 'target')])
    ## icmpv6-header.h: void ns3::Icmpv6NS::SetReserved(uint32_t reserved) [member function]
    cls.add_method('SetReserved', 
                   'void', 
                   [param('uint32_t', 'reserved')])
    return

def register_Ns3Icmpv6OptionHeader_methods(root_module, cls):
    ## icmpv6-header.h: ns3::Icmpv6OptionHeader::Icmpv6OptionHeader(ns3::Icmpv6OptionHeader const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv6OptionHeader const &', 'arg0')])
    ## icmpv6-header.h: ns3::Icmpv6OptionHeader::Icmpv6OptionHeader() [constructor]
    cls.add_constructor([])
    ## icmpv6-header.h: uint32_t ns3::Icmpv6OptionHeader::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv6-header.h: ns3::TypeId ns3::Icmpv6OptionHeader::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: uint8_t ns3::Icmpv6OptionHeader::GetLength() const [member function]
    cls.add_method('GetLength', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6OptionHeader::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: uint8_t ns3::Icmpv6OptionHeader::GetType() const [member function]
    cls.add_method('GetType', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: static ns3::TypeId ns3::Icmpv6OptionHeader::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv6-header.h: void ns3::Icmpv6OptionHeader::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6OptionHeader::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6OptionHeader::SetLength(uint8_t len) [member function]
    cls.add_method('SetLength', 
                   'void', 
                   [param('uint8_t', 'len')])
    ## icmpv6-header.h: void ns3::Icmpv6OptionHeader::SetType(uint8_t type) [member function]
    cls.add_method('SetType', 
                   'void', 
                   [param('uint8_t', 'type')])
    return

def register_Ns3Icmpv6OptionLinkLayerAddress_methods(root_module, cls):
    ## icmpv6-header.h: ns3::Icmpv6OptionLinkLayerAddress::Icmpv6OptionLinkLayerAddress(ns3::Icmpv6OptionLinkLayerAddress const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv6OptionLinkLayerAddress const &', 'arg0')])
    ## icmpv6-header.h: ns3::Icmpv6OptionLinkLayerAddress::Icmpv6OptionLinkLayerAddress(bool source) [constructor]
    cls.add_constructor([param('bool', 'source')])
    ## icmpv6-header.h: ns3::Icmpv6OptionLinkLayerAddress::Icmpv6OptionLinkLayerAddress(bool source, ns3::Address addr) [constructor]
    cls.add_constructor([param('bool', 'source'), param('ns3::Address', 'addr')])
    ## icmpv6-header.h: ns3::Icmpv6OptionLinkLayerAddress::Icmpv6OptionLinkLayerAddress() [constructor]
    cls.add_constructor([])
    ## icmpv6-header.h: uint32_t ns3::Icmpv6OptionLinkLayerAddress::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv6-header.h: ns3::Address ns3::Icmpv6OptionLinkLayerAddress::GetAddress() const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Address', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: ns3::TypeId ns3::Icmpv6OptionLinkLayerAddress::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6OptionLinkLayerAddress::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: static ns3::TypeId ns3::Icmpv6OptionLinkLayerAddress::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv6-header.h: void ns3::Icmpv6OptionLinkLayerAddress::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6OptionLinkLayerAddress::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6OptionLinkLayerAddress::SetAddress(ns3::Address addr) [member function]
    cls.add_method('SetAddress', 
                   'void', 
                   [param('ns3::Address', 'addr')])
    return

def register_Ns3Icmpv6OptionMtu_methods(root_module, cls):
    ## icmpv6-header.h: ns3::Icmpv6OptionMtu::Icmpv6OptionMtu(ns3::Icmpv6OptionMtu const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv6OptionMtu const &', 'arg0')])
    ## icmpv6-header.h: ns3::Icmpv6OptionMtu::Icmpv6OptionMtu() [constructor]
    cls.add_constructor([])
    ## icmpv6-header.h: ns3::Icmpv6OptionMtu::Icmpv6OptionMtu(uint32_t mtu) [constructor]
    cls.add_constructor([param('uint32_t', 'mtu')])
    ## icmpv6-header.h: uint32_t ns3::Icmpv6OptionMtu::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv6-header.h: ns3::TypeId ns3::Icmpv6OptionMtu::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6OptionMtu::GetMtu() const [member function]
    cls.add_method('GetMtu', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint16_t ns3::Icmpv6OptionMtu::GetReserved() const [member function]
    cls.add_method('GetReserved', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6OptionMtu::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: static ns3::TypeId ns3::Icmpv6OptionMtu::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv6-header.h: void ns3::Icmpv6OptionMtu::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6OptionMtu::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6OptionMtu::SetMtu(uint32_t mtu) [member function]
    cls.add_method('SetMtu', 
                   'void', 
                   [param('uint32_t', 'mtu')])
    ## icmpv6-header.h: void ns3::Icmpv6OptionMtu::SetReserved(uint16_t reserved) [member function]
    cls.add_method('SetReserved', 
                   'void', 
                   [param('uint16_t', 'reserved')])
    return

def register_Ns3Icmpv6OptionPrefixInformation_methods(root_module, cls):
    ## icmpv6-header.h: ns3::Icmpv6OptionPrefixInformation::Icmpv6OptionPrefixInformation(ns3::Icmpv6OptionPrefixInformation const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv6OptionPrefixInformation const &', 'arg0')])
    ## icmpv6-header.h: ns3::Icmpv6OptionPrefixInformation::Icmpv6OptionPrefixInformation() [constructor]
    cls.add_constructor([])
    ## icmpv6-header.h: ns3::Icmpv6OptionPrefixInformation::Icmpv6OptionPrefixInformation(ns3::Ipv6Address network, uint8_t prefixlen) [constructor]
    cls.add_constructor([param('ns3::Ipv6Address', 'network'), param('uint8_t', 'prefixlen')])
    ## icmpv6-header.h: uint32_t ns3::Icmpv6OptionPrefixInformation::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv6-header.h: uint8_t ns3::Icmpv6OptionPrefixInformation::GetFlags() const [member function]
    cls.add_method('GetFlags', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: ns3::TypeId ns3::Icmpv6OptionPrefixInformation::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6OptionPrefixInformation::GetPreferredTime() const [member function]
    cls.add_method('GetPreferredTime', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: ns3::Ipv6Address ns3::Icmpv6OptionPrefixInformation::GetPrefix() const [member function]
    cls.add_method('GetPrefix', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint8_t ns3::Icmpv6OptionPrefixInformation::GetPrefixLength() const [member function]
    cls.add_method('GetPrefixLength', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6OptionPrefixInformation::GetReserved() const [member function]
    cls.add_method('GetReserved', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6OptionPrefixInformation::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: static ns3::TypeId ns3::Icmpv6OptionPrefixInformation::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6OptionPrefixInformation::GetValidTime() const [member function]
    cls.add_method('GetValidTime', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: void ns3::Icmpv6OptionPrefixInformation::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6OptionPrefixInformation::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6OptionPrefixInformation::SetFlags(uint8_t flags) [member function]
    cls.add_method('SetFlags', 
                   'void', 
                   [param('uint8_t', 'flags')])
    ## icmpv6-header.h: void ns3::Icmpv6OptionPrefixInformation::SetPreferredTime(uint32_t preferredTime) [member function]
    cls.add_method('SetPreferredTime', 
                   'void', 
                   [param('uint32_t', 'preferredTime')])
    ## icmpv6-header.h: void ns3::Icmpv6OptionPrefixInformation::SetPrefix(ns3::Ipv6Address prefix) [member function]
    cls.add_method('SetPrefix', 
                   'void', 
                   [param('ns3::Ipv6Address', 'prefix')])
    ## icmpv6-header.h: void ns3::Icmpv6OptionPrefixInformation::SetPrefixLength(uint8_t prefixLength) [member function]
    cls.add_method('SetPrefixLength', 
                   'void', 
                   [param('uint8_t', 'prefixLength')])
    ## icmpv6-header.h: void ns3::Icmpv6OptionPrefixInformation::SetReserved(uint32_t reserved) [member function]
    cls.add_method('SetReserved', 
                   'void', 
                   [param('uint32_t', 'reserved')])
    ## icmpv6-header.h: void ns3::Icmpv6OptionPrefixInformation::SetValidTime(uint32_t validTime) [member function]
    cls.add_method('SetValidTime', 
                   'void', 
                   [param('uint32_t', 'validTime')])
    return

def register_Ns3Icmpv6OptionRedirected_methods(root_module, cls):
    ## icmpv6-header.h: ns3::Icmpv6OptionRedirected::Icmpv6OptionRedirected(ns3::Icmpv6OptionRedirected const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv6OptionRedirected const &', 'arg0')])
    ## icmpv6-header.h: ns3::Icmpv6OptionRedirected::Icmpv6OptionRedirected() [constructor]
    cls.add_constructor([])
    ## icmpv6-header.h: uint32_t ns3::Icmpv6OptionRedirected::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv6-header.h: ns3::TypeId ns3::Icmpv6OptionRedirected::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: ns3::Ptr<ns3::Packet> ns3::Icmpv6OptionRedirected::GetPacket() const [member function]
    cls.add_method('GetPacket', 
                   'ns3::Ptr< ns3::Packet >', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6OptionRedirected::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: static ns3::TypeId ns3::Icmpv6OptionRedirected::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv6-header.h: void ns3::Icmpv6OptionRedirected::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6OptionRedirected::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6OptionRedirected::SetPacket(ns3::Ptr<ns3::Packet> packet) [member function]
    cls.add_method('SetPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet')])
    return

def register_Ns3Icmpv6ParameterError_methods(root_module, cls):
    ## icmpv6-header.h: ns3::Icmpv6ParameterError::Icmpv6ParameterError(ns3::Icmpv6ParameterError const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv6ParameterError const &', 'arg0')])
    ## icmpv6-header.h: ns3::Icmpv6ParameterError::Icmpv6ParameterError() [constructor]
    cls.add_constructor([])
    ## icmpv6-header.h: uint32_t ns3::Icmpv6ParameterError::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv6-header.h: ns3::TypeId ns3::Icmpv6ParameterError::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: ns3::Ptr<ns3::Packet> ns3::Icmpv6ParameterError::GetPacket() const [member function]
    cls.add_method('GetPacket', 
                   'ns3::Ptr< ns3::Packet >', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6ParameterError::GetPtr() const [member function]
    cls.add_method('GetPtr', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6ParameterError::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: static ns3::TypeId ns3::Icmpv6ParameterError::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv6-header.h: void ns3::Icmpv6ParameterError::Print(std::ostream & os) [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6ParameterError::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6ParameterError::SetPacket(ns3::Ptr<ns3::Packet> p) [member function]
    cls.add_method('SetPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'p')])
    ## icmpv6-header.h: void ns3::Icmpv6ParameterError::SetPtr(uint32_t ptr) [member function]
    cls.add_method('SetPtr', 
                   'void', 
                   [param('uint32_t', 'ptr')])
    return

def register_Ns3Icmpv6RA_methods(root_module, cls):
    ## icmpv6-header.h: ns3::Icmpv6RA::Icmpv6RA(ns3::Icmpv6RA const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv6RA const &', 'arg0')])
    ## icmpv6-header.h: ns3::Icmpv6RA::Icmpv6RA() [constructor]
    cls.add_constructor([])
    ## icmpv6-header.h: uint32_t ns3::Icmpv6RA::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv6-header.h: uint8_t ns3::Icmpv6RA::GetCurHopLimit() const [member function]
    cls.add_method('GetCurHopLimit', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: bool ns3::Icmpv6RA::GetFlagH() const [member function]
    cls.add_method('GetFlagH', 
                   'bool', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: bool ns3::Icmpv6RA::GetFlagM() const [member function]
    cls.add_method('GetFlagM', 
                   'bool', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: bool ns3::Icmpv6RA::GetFlagO() const [member function]
    cls.add_method('GetFlagO', 
                   'bool', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint8_t ns3::Icmpv6RA::GetFlags() const [member function]
    cls.add_method('GetFlags', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: ns3::TypeId ns3::Icmpv6RA::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: uint16_t ns3::Icmpv6RA::GetLifeTime() const [member function]
    cls.add_method('GetLifeTime', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6RA::GetReachableTime() const [member function]
    cls.add_method('GetReachableTime', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6RA::GetRetransmissionTime() const [member function]
    cls.add_method('GetRetransmissionTime', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6RA::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: static ns3::TypeId ns3::Icmpv6RA::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv6-header.h: void ns3::Icmpv6RA::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6RA::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6RA::SetCurHopLimit(uint8_t m) [member function]
    cls.add_method('SetCurHopLimit', 
                   'void', 
                   [param('uint8_t', 'm')])
    ## icmpv6-header.h: void ns3::Icmpv6RA::SetFlagH(bool h) [member function]
    cls.add_method('SetFlagH', 
                   'void', 
                   [param('bool', 'h')])
    ## icmpv6-header.h: void ns3::Icmpv6RA::SetFlagM(bool m) [member function]
    cls.add_method('SetFlagM', 
                   'void', 
                   [param('bool', 'm')])
    ## icmpv6-header.h: void ns3::Icmpv6RA::SetFlagO(bool o) [member function]
    cls.add_method('SetFlagO', 
                   'void', 
                   [param('bool', 'o')])
    ## icmpv6-header.h: void ns3::Icmpv6RA::SetFlags(uint8_t f) [member function]
    cls.add_method('SetFlags', 
                   'void', 
                   [param('uint8_t', 'f')])
    ## icmpv6-header.h: void ns3::Icmpv6RA::SetLifeTime(uint16_t l) [member function]
    cls.add_method('SetLifeTime', 
                   'void', 
                   [param('uint16_t', 'l')])
    ## icmpv6-header.h: void ns3::Icmpv6RA::SetReachableTime(uint32_t r) [member function]
    cls.add_method('SetReachableTime', 
                   'void', 
                   [param('uint32_t', 'r')])
    ## icmpv6-header.h: void ns3::Icmpv6RA::SetRetransmissionTime(uint32_t r) [member function]
    cls.add_method('SetRetransmissionTime', 
                   'void', 
                   [param('uint32_t', 'r')])
    return

def register_Ns3Icmpv6RS_methods(root_module, cls):
    ## icmpv6-header.h: ns3::Icmpv6RS::Icmpv6RS(ns3::Icmpv6RS const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv6RS const &', 'arg0')])
    ## icmpv6-header.h: ns3::Icmpv6RS::Icmpv6RS() [constructor]
    cls.add_constructor([])
    ## icmpv6-header.h: uint32_t ns3::Icmpv6RS::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv6-header.h: ns3::TypeId ns3::Icmpv6RS::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6RS::GetReserved() const [member function]
    cls.add_method('GetReserved', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6RS::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: static ns3::TypeId ns3::Icmpv6RS::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv6-header.h: void ns3::Icmpv6RS::Print(std::ostream & os) [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6RS::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6RS::SetReserved(uint32_t reserved) [member function]
    cls.add_method('SetReserved', 
                   'void', 
                   [param('uint32_t', 'reserved')])
    return

def register_Ns3Icmpv6Redirection_methods(root_module, cls):
    ## icmpv6-header.h: ns3::Icmpv6Redirection::Icmpv6Redirection(ns3::Icmpv6Redirection const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv6Redirection const &', 'arg0')])
    ## icmpv6-header.h: ns3::Icmpv6Redirection::Icmpv6Redirection() [constructor]
    cls.add_constructor([])
    ## icmpv6-header.h: uint32_t ns3::Icmpv6Redirection::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv6-header.h: ns3::Ipv6Address ns3::Icmpv6Redirection::GetDestination() const [member function]
    cls.add_method('GetDestination', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: ns3::TypeId ns3::Icmpv6Redirection::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6Redirection::GetReserved() const [member function]
    cls.add_method('GetReserved', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6Redirection::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: ns3::Ipv6Address ns3::Icmpv6Redirection::GetTarget() const [member function]
    cls.add_method('GetTarget', 
                   'ns3::Ipv6Address', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: static ns3::TypeId ns3::Icmpv6Redirection::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv6-header.h: void ns3::Icmpv6Redirection::Print(std::ostream & os) [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6Redirection::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6Redirection::SetDestination(ns3::Ipv6Address destination) [member function]
    cls.add_method('SetDestination', 
                   'void', 
                   [param('ns3::Ipv6Address', 'destination')])
    ## icmpv6-header.h: void ns3::Icmpv6Redirection::SetReserved(uint32_t reserved) [member function]
    cls.add_method('SetReserved', 
                   'void', 
                   [param('uint32_t', 'reserved')])
    ## icmpv6-header.h: void ns3::Icmpv6Redirection::SetTarget(ns3::Ipv6Address target) [member function]
    cls.add_method('SetTarget', 
                   'void', 
                   [param('ns3::Ipv6Address', 'target')])
    return

def register_Ns3Icmpv6TimeExceeded_methods(root_module, cls):
    ## icmpv6-header.h: ns3::Icmpv6TimeExceeded::Icmpv6TimeExceeded(ns3::Icmpv6TimeExceeded const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv6TimeExceeded const &', 'arg0')])
    ## icmpv6-header.h: ns3::Icmpv6TimeExceeded::Icmpv6TimeExceeded() [constructor]
    cls.add_constructor([])
    ## icmpv6-header.h: uint32_t ns3::Icmpv6TimeExceeded::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv6-header.h: ns3::TypeId ns3::Icmpv6TimeExceeded::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: ns3::Ptr<ns3::Packet> ns3::Icmpv6TimeExceeded::GetPacket() const [member function]
    cls.add_method('GetPacket', 
                   'ns3::Ptr< ns3::Packet >', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6TimeExceeded::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: static ns3::TypeId ns3::Icmpv6TimeExceeded::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv6-header.h: void ns3::Icmpv6TimeExceeded::Print(std::ostream & os) [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6TimeExceeded::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6TimeExceeded::SetPacket(ns3::Ptr<ns3::Packet> p) [member function]
    cls.add_method('SetPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'p')])
    return

def register_Ns3Icmpv6TooBig_methods(root_module, cls):
    ## icmpv6-header.h: ns3::Icmpv6TooBig::Icmpv6TooBig(ns3::Icmpv6TooBig const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv6TooBig const &', 'arg0')])
    ## icmpv6-header.h: ns3::Icmpv6TooBig::Icmpv6TooBig() [constructor]
    cls.add_constructor([])
    ## icmpv6-header.h: uint32_t ns3::Icmpv6TooBig::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv6-header.h: ns3::TypeId ns3::Icmpv6TooBig::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6TooBig::GetMtu() const [member function]
    cls.add_method('GetMtu', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: ns3::Ptr<ns3::Packet> ns3::Icmpv6TooBig::GetPacket() const [member function]
    cls.add_method('GetPacket', 
                   'ns3::Ptr< ns3::Packet >', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6TooBig::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: static ns3::TypeId ns3::Icmpv6TooBig::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv6-header.h: void ns3::Icmpv6TooBig::Print(std::ostream & os) [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6TooBig::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6TooBig::SetMtu(uint32_t mtu) [member function]
    cls.add_method('SetMtu', 
                   'void', 
                   [param('uint32_t', 'mtu')])
    ## icmpv6-header.h: void ns3::Icmpv6TooBig::SetPacket(ns3::Ptr<ns3::Packet> p) [member function]
    cls.add_method('SetPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'p')])
    return

def register_Ns3TcpHeader_methods(root_module, cls):
    ## tcp-header.h: ns3::TcpHeader::TcpHeader(ns3::TcpHeader const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::TcpHeader const &', 'arg0')])
    ## tcp-header.h: ns3::TcpHeader::TcpHeader() [constructor]
    cls.add_constructor([])
    ## tcp-header.h: uint32_t ns3::TcpHeader::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## tcp-header.h: void ns3::TcpHeader::EnableChecksums() [member function]
    cls.add_method('EnableChecksums', 
                   'void', 
                   [])
    ## tcp-header.h: SequenceNumber ns3::TcpHeader::GetAckNumber() const [member function]
    cls.add_method('GetAckNumber', 
                   'SequenceNumber', 
                   [], 
                   is_const=True)
    ## tcp-header.h: uint16_t ns3::TcpHeader::GetDestinationPort() const [member function]
    cls.add_method('GetDestinationPort', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## tcp-header.h: uint8_t ns3::TcpHeader::GetFlags() const [member function]
    cls.add_method('GetFlags', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## tcp-header.h: ns3::TypeId ns3::TcpHeader::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## tcp-header.h: uint8_t ns3::TcpHeader::GetLength() const [member function]
    cls.add_method('GetLength', 
                   'uint8_t', 
                   [], 
                   is_const=True)
    ## tcp-header.h: SequenceNumber ns3::TcpHeader::GetSequenceNumber() const [member function]
    cls.add_method('GetSequenceNumber', 
                   'SequenceNumber', 
                   [], 
                   is_const=True)
    ## tcp-header.h: uint32_t ns3::TcpHeader::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## tcp-header.h: uint16_t ns3::TcpHeader::GetSourcePort() const [member function]
    cls.add_method('GetSourcePort', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## tcp-header.h: static ns3::TypeId ns3::TcpHeader::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## tcp-header.h: uint16_t ns3::TcpHeader::GetUrgentPointer() const [member function]
    cls.add_method('GetUrgentPointer', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## tcp-header.h: uint16_t ns3::TcpHeader::GetWindowSize() const [member function]
    cls.add_method('GetWindowSize', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## tcp-header.h: void ns3::TcpHeader::InitializeChecksum(ns3::Ipv4Address source, ns3::Ipv4Address destination, uint8_t protocol) [member function]
    cls.add_method('InitializeChecksum', 
                   'void', 
                   [param('ns3::Ipv4Address', 'source'), param('ns3::Ipv4Address', 'destination'), param('uint8_t', 'protocol')])
    ## tcp-header.h: bool ns3::TcpHeader::IsChecksumOk() const [member function]
    cls.add_method('IsChecksumOk', 
                   'bool', 
                   [], 
                   is_const=True)
    ## tcp-header.h: void ns3::TcpHeader::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## tcp-header.h: void ns3::TcpHeader::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## tcp-header.h: void ns3::TcpHeader::SetAckNumber(SequenceNumber ackNumber) [member function]
    cls.add_method('SetAckNumber', 
                   'void', 
                   [param('SequenceNumber', 'ackNumber')])
    ## tcp-header.h: void ns3::TcpHeader::SetDestinationPort(uint16_t port) [member function]
    cls.add_method('SetDestinationPort', 
                   'void', 
                   [param('uint16_t', 'port')])
    ## tcp-header.h: void ns3::TcpHeader::SetFlags(uint8_t flags) [member function]
    cls.add_method('SetFlags', 
                   'void', 
                   [param('uint8_t', 'flags')])
    ## tcp-header.h: void ns3::TcpHeader::SetLength(uint8_t length) [member function]
    cls.add_method('SetLength', 
                   'void', 
                   [param('uint8_t', 'length')])
    ## tcp-header.h: void ns3::TcpHeader::SetSequenceNumber(SequenceNumber sequenceNumber) [member function]
    cls.add_method('SetSequenceNumber', 
                   'void', 
                   [param('SequenceNumber', 'sequenceNumber')])
    ## tcp-header.h: void ns3::TcpHeader::SetSourcePort(uint16_t port) [member function]
    cls.add_method('SetSourcePort', 
                   'void', 
                   [param('uint16_t', 'port')])
    ## tcp-header.h: void ns3::TcpHeader::SetUrgentPointer(uint16_t urgentPointer) [member function]
    cls.add_method('SetUrgentPointer', 
                   'void', 
                   [param('uint16_t', 'urgentPointer')])
    ## tcp-header.h: void ns3::TcpHeader::SetWindowSize(uint16_t windowSize) [member function]
    cls.add_method('SetWindowSize', 
                   'void', 
                   [param('uint16_t', 'windowSize')])
    return

def register_Ns3UdpHeader_methods(root_module, cls):
    ## udp-header.h: ns3::UdpHeader::UdpHeader(ns3::UdpHeader const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UdpHeader const &', 'arg0')])
    ## udp-header.h: ns3::UdpHeader::UdpHeader() [constructor]
    cls.add_constructor([])
    ## udp-header.h: uint32_t ns3::UdpHeader::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## udp-header.h: void ns3::UdpHeader::EnableChecksums() [member function]
    cls.add_method('EnableChecksums', 
                   'void', 
                   [])
    ## udp-header.h: uint16_t ns3::UdpHeader::GetDestinationPort() const [member function]
    cls.add_method('GetDestinationPort', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## udp-header.h: ns3::TypeId ns3::UdpHeader::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## udp-header.h: uint32_t ns3::UdpHeader::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## udp-header.h: uint16_t ns3::UdpHeader::GetSourcePort() const [member function]
    cls.add_method('GetSourcePort', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## udp-header.h: static ns3::TypeId ns3::UdpHeader::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## udp-header.h: void ns3::UdpHeader::InitializeChecksum(ns3::Ipv4Address source, ns3::Ipv4Address destination, uint8_t protocol) [member function]
    cls.add_method('InitializeChecksum', 
                   'void', 
                   [param('ns3::Ipv4Address', 'source'), param('ns3::Ipv4Address', 'destination'), param('uint8_t', 'protocol')])
    ## udp-header.h: bool ns3::UdpHeader::IsChecksumOk() const [member function]
    cls.add_method('IsChecksumOk', 
                   'bool', 
                   [], 
                   is_const=True)
    ## udp-header.h: void ns3::UdpHeader::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## udp-header.h: void ns3::UdpHeader::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## udp-header.h: void ns3::UdpHeader::SetDestinationPort(uint16_t port) [member function]
    cls.add_method('SetDestinationPort', 
                   'void', 
                   [param('uint16_t', 'port')])
    ## udp-header.h: void ns3::UdpHeader::SetSourcePort(uint16_t port) [member function]
    cls.add_method('SetSourcePort', 
                   'void', 
                   [param('uint16_t', 'port')])
    return

def register_Ns3ArpCache_methods(root_module, cls):
    ## arp-cache.h: ns3::ArpCache::ArpCache() [constructor]
    cls.add_constructor([])
    ## arp-cache.h: ns3::ArpCache::Entry * ns3::ArpCache::Add(ns3::Ipv4Address to) [member function]
    cls.add_method('Add', 
                   'ns3::ArpCache::Entry *', 
                   [param('ns3::Ipv4Address', 'to')])
    ## arp-cache.h: void ns3::ArpCache::Flush() [member function]
    cls.add_method('Flush', 
                   'void', 
                   [])
    ## arp-cache.h: ns3::Time ns3::ArpCache::GetAliveTimeout() const [member function]
    cls.add_method('GetAliveTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## arp-cache.h: ns3::Time ns3::ArpCache::GetDeadTimeout() const [member function]
    cls.add_method('GetDeadTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## arp-cache.h: ns3::Ptr<ns3::NetDevice> ns3::ArpCache::GetDevice() const [member function]
    cls.add_method('GetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [], 
                   is_const=True)
    ## arp-cache.h: ns3::Ptr<ns3::Ipv4Interface> ns3::ArpCache::GetInterface() const [member function]
    cls.add_method('GetInterface', 
                   'ns3::Ptr< ns3::Ipv4Interface >', 
                   [], 
                   is_const=True)
    ## arp-cache.h: static ns3::TypeId ns3::ArpCache::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## arp-cache.h: ns3::Time ns3::ArpCache::GetWaitReplyTimeout() const [member function]
    cls.add_method('GetWaitReplyTimeout', 
                   'ns3::Time', 
                   [], 
                   is_const=True)
    ## arp-cache.h: ns3::ArpCache::Entry * ns3::ArpCache::Lookup(ns3::Ipv4Address destination) [member function]
    cls.add_method('Lookup', 
                   'ns3::ArpCache::Entry *', 
                   [param('ns3::Ipv4Address', 'destination')])
    ## arp-cache.h: void ns3::ArpCache::SetAliveTimeout(ns3::Time aliveTimeout) [member function]
    cls.add_method('SetAliveTimeout', 
                   'void', 
                   [param('ns3::Time', 'aliveTimeout')])
    ## arp-cache.h: void ns3::ArpCache::SetArpRequestCallback(ns3::Callback<void, ns3::Ptr<ns3::ArpCache const>, ns3::Ipv4Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty> arpRequestCallback) [member function]
    cls.add_method('SetArpRequestCallback', 
                   'void', 
                   [param('ns3::Callback< void, ns3::Ptr< ns3::ArpCache const >, ns3::Ipv4Address, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty, ns3::empty >', 'arpRequestCallback')])
    ## arp-cache.h: void ns3::ArpCache::SetDeadTimeout(ns3::Time deadTimeout) [member function]
    cls.add_method('SetDeadTimeout', 
                   'void', 
                   [param('ns3::Time', 'deadTimeout')])
    ## arp-cache.h: void ns3::ArpCache::SetDevice(ns3::Ptr<ns3::NetDevice> device, ns3::Ptr<ns3::Ipv4Interface> interface) [member function]
    cls.add_method('SetDevice', 
                   'void', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device'), param('ns3::Ptr< ns3::Ipv4Interface >', 'interface')])
    ## arp-cache.h: void ns3::ArpCache::SetWaitReplyTimeout(ns3::Time waitReplyTimeout) [member function]
    cls.add_method('SetWaitReplyTimeout', 
                   'void', 
                   [param('ns3::Time', 'waitReplyTimeout')])
    ## arp-cache.h: void ns3::ArpCache::StartWaitReplyTimer() [member function]
    cls.add_method('StartWaitReplyTimer', 
                   'void', 
                   [])
    ## arp-cache.h: void ns3::ArpCache::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_Ns3ArpCacheEntry_methods(root_module, cls):
    ## arp-cache.h: ns3::ArpCache::Entry::Entry(ns3::ArpCache::Entry const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::ArpCache::Entry const &', 'arg0')])
    ## arp-cache.h: ns3::ArpCache::Entry::Entry(ns3::ArpCache * arp) [constructor]
    cls.add_constructor([param('ns3::ArpCache *', 'arp')])
    ## arp-cache.h: void ns3::ArpCache::Entry::ClearRetries() [member function]
    cls.add_method('ClearRetries', 
                   'void', 
                   [])
    ## arp-cache.h: ns3::Ptr<ns3::Packet> ns3::ArpCache::Entry::DequeuePending() [member function]
    cls.add_method('DequeuePending', 
                   'ns3::Ptr< ns3::Packet >', 
                   [])
    ## arp-cache.h: ns3::Ipv4Address ns3::ArpCache::Entry::GetIpv4Address() const [member function]
    cls.add_method('GetIpv4Address', 
                   'ns3::Ipv4Address', 
                   [], 
                   is_const=True)
    ## arp-cache.h: ns3::Address ns3::ArpCache::Entry::GetMacAddress() const [member function]
    cls.add_method('GetMacAddress', 
                   'ns3::Address', 
                   [], 
                   is_const=True)
    ## arp-cache.h: uint32_t ns3::ArpCache::Entry::GetRetries() const [member function]
    cls.add_method('GetRetries', 
                   'uint32_t', 
                   [], 
                   is_const=True)
    ## arp-cache.h: void ns3::ArpCache::Entry::IncrementRetries() [member function]
    cls.add_method('IncrementRetries', 
                   'void', 
                   [])
    ## arp-cache.h: bool ns3::ArpCache::Entry::IsAlive() [member function]
    cls.add_method('IsAlive', 
                   'bool', 
                   [])
    ## arp-cache.h: bool ns3::ArpCache::Entry::IsDead() [member function]
    cls.add_method('IsDead', 
                   'bool', 
                   [])
    ## arp-cache.h: bool ns3::ArpCache::Entry::IsExpired() const [member function]
    cls.add_method('IsExpired', 
                   'bool', 
                   [], 
                   is_const=True)
    ## arp-cache.h: bool ns3::ArpCache::Entry::IsWaitReply() [member function]
    cls.add_method('IsWaitReply', 
                   'bool', 
                   [])
    ## arp-cache.h: void ns3::ArpCache::Entry::MarkAlive(ns3::Address macAddress) [member function]
    cls.add_method('MarkAlive', 
                   'void', 
                   [param('ns3::Address', 'macAddress')])
    ## arp-cache.h: void ns3::ArpCache::Entry::MarkDead() [member function]
    cls.add_method('MarkDead', 
                   'void', 
                   [])
    ## arp-cache.h: void ns3::ArpCache::Entry::MarkWaitReply(ns3::Ptr<ns3::Packet> waiting) [member function]
    cls.add_method('MarkWaitReply', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'waiting')])
    ## arp-cache.h: void ns3::ArpCache::Entry::SetIpv4Address(ns3::Ipv4Address destination) [member function]
    cls.add_method('SetIpv4Address', 
                   'void', 
                   [param('ns3::Ipv4Address', 'destination')])
    ## arp-cache.h: bool ns3::ArpCache::Entry::UpdateWaitReply(ns3::Ptr<ns3::Packet> waiting) [member function]
    cls.add_method('UpdateWaitReply', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'waiting')])
    return

def register_Ns3ArpL3Protocol_methods(root_module, cls):
    ## arp-l3-protocol.h: ns3::ArpL3Protocol::PROT_NUMBER [variable]
    cls.add_static_attribute('PROT_NUMBER', 'uint16_t const', is_const=True)
    ## arp-l3-protocol.h: static ns3::TypeId ns3::ArpL3Protocol::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## arp-l3-protocol.h: ns3::ArpL3Protocol::ArpL3Protocol() [constructor]
    cls.add_constructor([])
    ## arp-l3-protocol.h: void ns3::ArpL3Protocol::SetNode(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('SetNode', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')])
    ## arp-l3-protocol.h: ns3::Ptr<ns3::ArpCache> ns3::ArpL3Protocol::CreateCache(ns3::Ptr<ns3::NetDevice> device, ns3::Ptr<ns3::Ipv4Interface> interface) [member function]
    cls.add_method('CreateCache', 
                   'ns3::Ptr< ns3::ArpCache >', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device'), param('ns3::Ptr< ns3::Ipv4Interface >', 'interface')])
    ## arp-l3-protocol.h: void ns3::ArpL3Protocol::Receive(ns3::Ptr<ns3::NetDevice> device, ns3::Ptr<ns3::Packet const> p, uint16_t protocol, ns3::Address const & from, ns3::Address const & to, ns3::NetDevice::PacketType packetType) [member function]
    cls.add_method('Receive', 
                   'void', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device'), param('ns3::Ptr< ns3::Packet const >', 'p'), param('uint16_t', 'protocol'), param('ns3::Address const &', 'from'), param('ns3::Address const &', 'to'), param('ns3::NetDevice::PacketType', 'packetType')])
    ## arp-l3-protocol.h: bool ns3::ArpL3Protocol::Lookup(ns3::Ptr<ns3::Packet> p, ns3::Ipv4Address destination, ns3::Ptr<ns3::NetDevice> device, ns3::Ptr<ns3::ArpCache> cache, ns3::Address * hardwareDestination) [member function]
    cls.add_method('Lookup', 
                   'bool', 
                   [param('ns3::Ptr< ns3::Packet >', 'p'), param('ns3::Ipv4Address', 'destination'), param('ns3::Ptr< ns3::NetDevice >', 'device'), param('ns3::Ptr< ns3::ArpCache >', 'cache'), param('ns3::Address *', 'hardwareDestination')])
    ## arp-l3-protocol.h: void ns3::ArpL3Protocol::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## arp-l3-protocol.h: void ns3::ArpL3Protocol::NotifyNewAggregate() [member function]
    cls.add_method('NotifyNewAggregate', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3Icmpv6DestinationUnreachable_methods(root_module, cls):
    ## icmpv6-header.h: ns3::Icmpv6DestinationUnreachable::Icmpv6DestinationUnreachable(ns3::Icmpv6DestinationUnreachable const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv6DestinationUnreachable const &', 'arg0')])
    ## icmpv6-header.h: ns3::Icmpv6DestinationUnreachable::Icmpv6DestinationUnreachable() [constructor]
    cls.add_constructor([])
    ## icmpv6-header.h: uint32_t ns3::Icmpv6DestinationUnreachable::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv6-header.h: ns3::TypeId ns3::Icmpv6DestinationUnreachable::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: ns3::Ptr<ns3::Packet> ns3::Icmpv6DestinationUnreachable::GetPacket() const [member function]
    cls.add_method('GetPacket', 
                   'ns3::Ptr< ns3::Packet >', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6DestinationUnreachable::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: static ns3::TypeId ns3::Icmpv6DestinationUnreachable::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv6-header.h: void ns3::Icmpv6DestinationUnreachable::Print(std::ostream & os) [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6DestinationUnreachable::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6DestinationUnreachable::SetPacket(ns3::Ptr<ns3::Packet> p) [member function]
    cls.add_method('SetPacket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'p')])
    return

def register_Ns3Icmpv6Echo_methods(root_module, cls):
    ## icmpv6-header.h: ns3::Icmpv6Echo::Icmpv6Echo(ns3::Icmpv6Echo const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv6Echo const &', 'arg0')])
    ## icmpv6-header.h: ns3::Icmpv6Echo::Icmpv6Echo() [constructor]
    cls.add_constructor([])
    ## icmpv6-header.h: ns3::Icmpv6Echo::Icmpv6Echo(bool request) [constructor]
    cls.add_constructor([param('bool', 'request')])
    ## icmpv6-header.h: uint32_t ns3::Icmpv6Echo::Deserialize(ns3::Buffer::Iterator start) [member function]
    cls.add_method('Deserialize', 
                   'uint32_t', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_virtual=True)
    ## icmpv6-header.h: uint16_t ns3::Icmpv6Echo::GetId() const [member function]
    cls.add_method('GetId', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: ns3::TypeId ns3::Icmpv6Echo::GetInstanceTypeId() const [member function]
    cls.add_method('GetInstanceTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: uint16_t ns3::Icmpv6Echo::GetSeq() const [member function]
    cls.add_method('GetSeq', 
                   'uint16_t', 
                   [], 
                   is_const=True)
    ## icmpv6-header.h: uint32_t ns3::Icmpv6Echo::GetSerializedSize() const [member function]
    cls.add_method('GetSerializedSize', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: static ns3::TypeId ns3::Icmpv6Echo::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv6-header.h: void ns3::Icmpv6Echo::Print(std::ostream & os) const [member function]
    cls.add_method('Print', 
                   'void', 
                   [param('std::ostream &', 'os')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6Echo::Serialize(ns3::Buffer::Iterator start) const [member function]
    cls.add_method('Serialize', 
                   'void', 
                   [param('ns3::Buffer::Iterator', 'start')], 
                   is_const=True, is_virtual=True)
    ## icmpv6-header.h: void ns3::Icmpv6Echo::SetId(uint16_t id) [member function]
    cls.add_method('SetId', 
                   'void', 
                   [param('uint16_t', 'id')])
    ## icmpv6-header.h: void ns3::Icmpv6Echo::SetSeq(uint16_t seq) [member function]
    cls.add_method('SetSeq', 
                   'void', 
                   [param('uint16_t', 'seq')])
    return

def register_Ns3Ipv4L3Protocol_methods(root_module, cls):
    ## ipv4-l3-protocol.h: ns3::Ipv4L3Protocol::PROT_NUMBER [variable]
    cls.add_static_attribute('PROT_NUMBER', 'uint16_t const', is_const=True)
    ## ipv4-l3-protocol.h: static ns3::TypeId ns3::Ipv4L3Protocol::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## ipv4-l3-protocol.h: ns3::Ipv4L3Protocol::Ipv4L3Protocol() [constructor]
    cls.add_constructor([])
    ## ipv4-l3-protocol.h: void ns3::Ipv4L3Protocol::SetNode(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('SetNode', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')])
    ## ipv4-l3-protocol.h: void ns3::Ipv4L3Protocol::SetRoutingProtocol(ns3::Ptr<ns3::Ipv4RoutingProtocol> routingProtocol) [member function]
    cls.add_method('SetRoutingProtocol', 
                   'void', 
                   [param('ns3::Ptr< ns3::Ipv4RoutingProtocol >', 'routingProtocol')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h: ns3::Ptr<ns3::Ipv4RoutingProtocol> ns3::Ipv4L3Protocol::GetRoutingProtocol() const [member function]
    cls.add_method('GetRoutingProtocol', 
                   'ns3::Ptr< ns3::Ipv4RoutingProtocol >', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h: ns3::Ptr<ns3::Socket> ns3::Ipv4L3Protocol::CreateRawSocket() [member function]
    cls.add_method('CreateRawSocket', 
                   'ns3::Ptr< ns3::Socket >', 
                   [])
    ## ipv4-l3-protocol.h: void ns3::Ipv4L3Protocol::DeleteRawSocket(ns3::Ptr<ns3::Socket> socket) [member function]
    cls.add_method('DeleteRawSocket', 
                   'void', 
                   [param('ns3::Ptr< ns3::Socket >', 'socket')])
    ## ipv4-l3-protocol.h: void ns3::Ipv4L3Protocol::Insert(ns3::Ptr<ns3::Ipv4L4Protocol> protocol) [member function]
    cls.add_method('Insert', 
                   'void', 
                   [param('ns3::Ptr< ns3::Ipv4L4Protocol >', 'protocol')])
    ## ipv4-l3-protocol.h: ns3::Ptr<ns3::Ipv4L4Protocol> ns3::Ipv4L3Protocol::GetProtocol(int protocolNumber) const [member function]
    cls.add_method('GetProtocol', 
                   'ns3::Ptr< ns3::Ipv4L4Protocol >', 
                   [param('int', 'protocolNumber')], 
                   is_const=True)
    ## ipv4-l3-protocol.h: void ns3::Ipv4L3Protocol::Remove(ns3::Ptr<ns3::Ipv4L4Protocol> protocol) [member function]
    cls.add_method('Remove', 
                   'void', 
                   [param('ns3::Ptr< ns3::Ipv4L4Protocol >', 'protocol')])
    ## ipv4-l3-protocol.h: void ns3::Ipv4L3Protocol::SetDefaultTtl(uint8_t ttl) [member function]
    cls.add_method('SetDefaultTtl', 
                   'void', 
                   [param('uint8_t', 'ttl')])
    ## ipv4-l3-protocol.h: void ns3::Ipv4L3Protocol::Receive(ns3::Ptr<ns3::NetDevice> device, ns3::Ptr<ns3::Packet const> p, uint16_t protocol, ns3::Address const & from, ns3::Address const & to, ns3::NetDevice::PacketType packetType) [member function]
    cls.add_method('Receive', 
                   'void', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device'), param('ns3::Ptr< ns3::Packet const >', 'p'), param('uint16_t', 'protocol'), param('ns3::Address const &', 'from'), param('ns3::Address const &', 'to'), param('ns3::NetDevice::PacketType', 'packetType')])
    ## ipv4-l3-protocol.h: void ns3::Ipv4L3Protocol::Send(ns3::Ptr<ns3::Packet> packet, ns3::Ipv4Address source, ns3::Ipv4Address destination, uint8_t protocol, ns3::Ptr<ns3::Ipv4Route> route) [member function]
    cls.add_method('Send', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Ipv4Address', 'source'), param('ns3::Ipv4Address', 'destination'), param('uint8_t', 'protocol'), param('ns3::Ptr< ns3::Ipv4Route >', 'route')])
    ## ipv4-l3-protocol.h: uint32_t ns3::Ipv4L3Protocol::AddInterface(ns3::Ptr<ns3::NetDevice> device) [member function]
    cls.add_method('AddInterface', 
                   'uint32_t', 
                   [param('ns3::Ptr< ns3::NetDevice >', 'device')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h: ns3::Ptr<ns3::Ipv4Interface> ns3::Ipv4L3Protocol::GetInterface(uint32_t i) const [member function]
    cls.add_method('GetInterface', 
                   'ns3::Ptr< ns3::Ipv4Interface >', 
                   [param('uint32_t', 'i')], 
                   is_const=True)
    ## ipv4-l3-protocol.h: uint32_t ns3::Ipv4L3Protocol::GetNInterfaces() const [member function]
    cls.add_method('GetNInterfaces', 
                   'uint32_t', 
                   [], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h: int32_t ns3::Ipv4L3Protocol::GetInterfaceForAddress(ns3::Ipv4Address addr) const [member function]
    cls.add_method('GetInterfaceForAddress', 
                   'int32_t', 
                   [param('ns3::Ipv4Address', 'addr')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h: int32_t ns3::Ipv4L3Protocol::GetInterfaceForPrefix(ns3::Ipv4Address addr, ns3::Ipv4Mask mask) const [member function]
    cls.add_method('GetInterfaceForPrefix', 
                   'int32_t', 
                   [param('ns3::Ipv4Address', 'addr'), param('ns3::Ipv4Mask', 'mask')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h: int32_t ns3::Ipv4L3Protocol::GetInterfaceForDevice(ns3::Ptr<const ns3::NetDevice> device) const [member function]
    cls.add_method('GetInterfaceForDevice', 
                   'int32_t', 
                   [param('ns3::Ptr< ns3::NetDevice const >', 'device')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h: bool ns3::Ipv4L3Protocol::AddAddress(uint32_t i, ns3::Ipv4InterfaceAddress address) [member function]
    cls.add_method('AddAddress', 
                   'bool', 
                   [param('uint32_t', 'i'), param('ns3::Ipv4InterfaceAddress', 'address')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h: ns3::Ipv4InterfaceAddress ns3::Ipv4L3Protocol::GetAddress(uint32_t interfaceIndex, uint32_t addressIndex) const [member function]
    cls.add_method('GetAddress', 
                   'ns3::Ipv4InterfaceAddress', 
                   [param('uint32_t', 'interfaceIndex'), param('uint32_t', 'addressIndex')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h: uint32_t ns3::Ipv4L3Protocol::GetNAddresses(uint32_t interface) const [member function]
    cls.add_method('GetNAddresses', 
                   'uint32_t', 
                   [param('uint32_t', 'interface')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h: bool ns3::Ipv4L3Protocol::RemoveAddress(uint32_t interfaceIndex, uint32_t addressIndex) [member function]
    cls.add_method('RemoveAddress', 
                   'bool', 
                   [param('uint32_t', 'interfaceIndex'), param('uint32_t', 'addressIndex')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h: void ns3::Ipv4L3Protocol::SetMetric(uint32_t i, uint16_t metric) [member function]
    cls.add_method('SetMetric', 
                   'void', 
                   [param('uint32_t', 'i'), param('uint16_t', 'metric')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h: uint16_t ns3::Ipv4L3Protocol::GetMetric(uint32_t i) const [member function]
    cls.add_method('GetMetric', 
                   'uint16_t', 
                   [param('uint32_t', 'i')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h: uint16_t ns3::Ipv4L3Protocol::GetMtu(uint32_t i) const [member function]
    cls.add_method('GetMtu', 
                   'uint16_t', 
                   [param('uint32_t', 'i')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h: bool ns3::Ipv4L3Protocol::IsUp(uint32_t i) const [member function]
    cls.add_method('IsUp', 
                   'bool', 
                   [param('uint32_t', 'i')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h: void ns3::Ipv4L3Protocol::SetUp(uint32_t i) [member function]
    cls.add_method('SetUp', 
                   'void', 
                   [param('uint32_t', 'i')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h: void ns3::Ipv4L3Protocol::SetDown(uint32_t i) [member function]
    cls.add_method('SetDown', 
                   'void', 
                   [param('uint32_t', 'i')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h: bool ns3::Ipv4L3Protocol::IsForwarding(uint32_t i) const [member function]
    cls.add_method('IsForwarding', 
                   'bool', 
                   [param('uint32_t', 'i')], 
                   is_const=True, is_virtual=True)
    ## ipv4-l3-protocol.h: void ns3::Ipv4L3Protocol::SetForwarding(uint32_t i, bool val) [member function]
    cls.add_method('SetForwarding', 
                   'void', 
                   [param('uint32_t', 'i'), param('bool', 'val')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h: ns3::Ptr<ns3::NetDevice> ns3::Ipv4L3Protocol::GetNetDevice(uint32_t i) [member function]
    cls.add_method('GetNetDevice', 
                   'ns3::Ptr< ns3::NetDevice >', 
                   [param('uint32_t', 'i')], 
                   is_virtual=True)
    ## ipv4-l3-protocol.h: void ns3::Ipv4L3Protocol::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## ipv4-l3-protocol.h: void ns3::Ipv4L3Protocol::NotifyNewAggregate() [member function]
    cls.add_method('NotifyNewAggregate', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## ipv4-l3-protocol.h: void ns3::Ipv4L3Protocol::SetIpForward(bool forward) [member function]
    cls.add_method('SetIpForward', 
                   'void', 
                   [param('bool', 'forward')], 
                   visibility='private', is_virtual=True)
    ## ipv4-l3-protocol.h: bool ns3::Ipv4L3Protocol::GetIpForward() const [member function]
    cls.add_method('GetIpForward', 
                   'bool', 
                   [], 
                   is_const=True, visibility='private', is_virtual=True)
    return

def register_Ns3Ipv4L4Protocol_methods(root_module, cls):
    ## ipv4-l4-protocol.h: ns3::Ipv4L4Protocol::Ipv4L4Protocol() [constructor]
    cls.add_constructor([])
    ## ipv4-l4-protocol.h: ns3::Ipv4L4Protocol::Ipv4L4Protocol(ns3::Ipv4L4Protocol const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Ipv4L4Protocol const &', 'arg0')])
    ## ipv4-l4-protocol.h: int ns3::Ipv4L4Protocol::GetProtocolNumber() const [member function]
    cls.add_method('GetProtocolNumber', 
                   'int', 
                   [], 
                   is_pure_virtual=True, is_const=True, is_virtual=True)
    ## ipv4-l4-protocol.h: static ns3::TypeId ns3::Ipv4L4Protocol::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## ipv4-l4-protocol.h: ns3::Ipv4L4Protocol::RxStatus ns3::Ipv4L4Protocol::Receive(ns3::Ptr<ns3::Packet> p, ns3::Ipv4Address const & source, ns3::Ipv4Address const & destination, ns3::Ptr<ns3::Ipv4Interface> incomingInterface) [member function]
    cls.add_method('Receive', 
                   'ns3::Ipv4L4Protocol::RxStatus', 
                   [param('ns3::Ptr< ns3::Packet >', 'p'), param('ns3::Ipv4Address const &', 'source'), param('ns3::Ipv4Address const &', 'destination'), param('ns3::Ptr< ns3::Ipv4Interface >', 'incomingInterface')], 
                   is_pure_virtual=True, is_virtual=True)
    ## ipv4-l4-protocol.h: void ns3::Ipv4L4Protocol::ReceiveIcmp(ns3::Ipv4Address icmpSource, uint8_t icmpTtl, uint8_t icmpType, uint8_t icmpCode, uint32_t icmpInfo, ns3::Ipv4Address payloadSource, ns3::Ipv4Address payloadDestination, uint8_t const * payload) [member function]
    cls.add_method('ReceiveIcmp', 
                   'void', 
                   [param('ns3::Ipv4Address', 'icmpSource'), param('uint8_t', 'icmpTtl'), param('uint8_t', 'icmpType'), param('uint8_t', 'icmpCode'), param('uint32_t', 'icmpInfo'), param('ns3::Ipv4Address', 'payloadSource'), param('ns3::Ipv4Address', 'payloadDestination'), param('uint8_t const *', 'payload')], 
                   is_virtual=True)
    return

def register_Ns3TcpL4Protocol_methods(root_module, cls):
    ## tcp-l4-protocol.h: ns3::TcpL4Protocol::PROT_NUMBER [variable]
    cls.add_static_attribute('PROT_NUMBER', 'uint8_t const', is_const=True)
    ## tcp-l4-protocol.h: static ns3::TypeId ns3::TcpL4Protocol::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## tcp-l4-protocol.h: ns3::TcpL4Protocol::TcpL4Protocol() [constructor]
    cls.add_constructor([])
    ## tcp-l4-protocol.h: void ns3::TcpL4Protocol::SetNode(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('SetNode', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')])
    ## tcp-l4-protocol.h: int ns3::TcpL4Protocol::GetProtocolNumber() const [member function]
    cls.add_method('GetProtocolNumber', 
                   'int', 
                   [], 
                   is_const=True, is_virtual=True)
    ## tcp-l4-protocol.h: ns3::Ptr<ns3::Socket> ns3::TcpL4Protocol::CreateSocket() [member function]
    cls.add_method('CreateSocket', 
                   'ns3::Ptr< ns3::Socket >', 
                   [])
    ## tcp-l4-protocol.h: ns3::Ipv4EndPoint * ns3::TcpL4Protocol::Allocate() [member function]
    cls.add_method('Allocate', 
                   'ns3::Ipv4EndPoint *', 
                   [])
    ## tcp-l4-protocol.h: ns3::Ipv4EndPoint * ns3::TcpL4Protocol::Allocate(ns3::Ipv4Address address) [member function]
    cls.add_method('Allocate', 
                   'ns3::Ipv4EndPoint *', 
                   [param('ns3::Ipv4Address', 'address')])
    ## tcp-l4-protocol.h: ns3::Ipv4EndPoint * ns3::TcpL4Protocol::Allocate(uint16_t port) [member function]
    cls.add_method('Allocate', 
                   'ns3::Ipv4EndPoint *', 
                   [param('uint16_t', 'port')])
    ## tcp-l4-protocol.h: ns3::Ipv4EndPoint * ns3::TcpL4Protocol::Allocate(ns3::Ipv4Address address, uint16_t port) [member function]
    cls.add_method('Allocate', 
                   'ns3::Ipv4EndPoint *', 
                   [param('ns3::Ipv4Address', 'address'), param('uint16_t', 'port')])
    ## tcp-l4-protocol.h: ns3::Ipv4EndPoint * ns3::TcpL4Protocol::Allocate(ns3::Ipv4Address localAddress, uint16_t localPort, ns3::Ipv4Address peerAddress, uint16_t peerPort) [member function]
    cls.add_method('Allocate', 
                   'ns3::Ipv4EndPoint *', 
                   [param('ns3::Ipv4Address', 'localAddress'), param('uint16_t', 'localPort'), param('ns3::Ipv4Address', 'peerAddress'), param('uint16_t', 'peerPort')])
    ## tcp-l4-protocol.h: void ns3::TcpL4Protocol::DeAllocate(ns3::Ipv4EndPoint * endPoint) [member function]
    cls.add_method('DeAllocate', 
                   'void', 
                   [param('ns3::Ipv4EndPoint *', 'endPoint')])
    ## tcp-l4-protocol.h: void ns3::TcpL4Protocol::Send(ns3::Ptr<ns3::Packet> packet, ns3::Ipv4Address saddr, ns3::Ipv4Address daddr, uint16_t sport, uint16_t dport) [member function]
    cls.add_method('Send', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Ipv4Address', 'saddr'), param('ns3::Ipv4Address', 'daddr'), param('uint16_t', 'sport'), param('uint16_t', 'dport')])
    ## tcp-l4-protocol.h: ns3::Ipv4L4Protocol::RxStatus ns3::TcpL4Protocol::Receive(ns3::Ptr<ns3::Packet> p, ns3::Ipv4Address const & source, ns3::Ipv4Address const & destination, ns3::Ptr<ns3::Ipv4Interface> incomingInterface) [member function]
    cls.add_method('Receive', 
                   'ns3::Ipv4L4Protocol::RxStatus', 
                   [param('ns3::Ptr< ns3::Packet >', 'p'), param('ns3::Ipv4Address const &', 'source'), param('ns3::Ipv4Address const &', 'destination'), param('ns3::Ptr< ns3::Ipv4Interface >', 'incomingInterface')], 
                   is_virtual=True)
    ## tcp-l4-protocol.h: void ns3::TcpL4Protocol::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## tcp-l4-protocol.h: void ns3::TcpL4Protocol::NotifyNewAggregate() [member function]
    cls.add_method('NotifyNewAggregate', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3UdpL4Protocol_methods(root_module, cls):
    ## udp-l4-protocol.h: ns3::UdpL4Protocol::UdpL4Protocol(ns3::UdpL4Protocol const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::UdpL4Protocol const &', 'arg0')])
    ## udp-l4-protocol.h: ns3::UdpL4Protocol::UdpL4Protocol() [constructor]
    cls.add_constructor([])
    ## udp-l4-protocol.h: ns3::Ipv4EndPoint * ns3::UdpL4Protocol::Allocate() [member function]
    cls.add_method('Allocate', 
                   'ns3::Ipv4EndPoint *', 
                   [])
    ## udp-l4-protocol.h: ns3::Ipv4EndPoint * ns3::UdpL4Protocol::Allocate(ns3::Ipv4Address address) [member function]
    cls.add_method('Allocate', 
                   'ns3::Ipv4EndPoint *', 
                   [param('ns3::Ipv4Address', 'address')])
    ## udp-l4-protocol.h: ns3::Ipv4EndPoint * ns3::UdpL4Protocol::Allocate(uint16_t port) [member function]
    cls.add_method('Allocate', 
                   'ns3::Ipv4EndPoint *', 
                   [param('uint16_t', 'port')])
    ## udp-l4-protocol.h: ns3::Ipv4EndPoint * ns3::UdpL4Protocol::Allocate(ns3::Ipv4Address address, uint16_t port) [member function]
    cls.add_method('Allocate', 
                   'ns3::Ipv4EndPoint *', 
                   [param('ns3::Ipv4Address', 'address'), param('uint16_t', 'port')])
    ## udp-l4-protocol.h: ns3::Ipv4EndPoint * ns3::UdpL4Protocol::Allocate(ns3::Ipv4Address localAddress, uint16_t localPort, ns3::Ipv4Address peerAddress, uint16_t peerPort) [member function]
    cls.add_method('Allocate', 
                   'ns3::Ipv4EndPoint *', 
                   [param('ns3::Ipv4Address', 'localAddress'), param('uint16_t', 'localPort'), param('ns3::Ipv4Address', 'peerAddress'), param('uint16_t', 'peerPort')])
    ## udp-l4-protocol.h: ns3::Ptr<ns3::Socket> ns3::UdpL4Protocol::CreateSocket() [member function]
    cls.add_method('CreateSocket', 
                   'ns3::Ptr< ns3::Socket >', 
                   [])
    ## udp-l4-protocol.h: void ns3::UdpL4Protocol::DeAllocate(ns3::Ipv4EndPoint * endPoint) [member function]
    cls.add_method('DeAllocate', 
                   'void', 
                   [param('ns3::Ipv4EndPoint *', 'endPoint')])
    ## udp-l4-protocol.h: int ns3::UdpL4Protocol::GetProtocolNumber() const [member function]
    cls.add_method('GetProtocolNumber', 
                   'int', 
                   [], 
                   is_const=True, is_virtual=True)
    ## udp-l4-protocol.h: static ns3::TypeId ns3::UdpL4Protocol::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## udp-l4-protocol.h: ns3::Ipv4L4Protocol::RxStatus ns3::UdpL4Protocol::Receive(ns3::Ptr<ns3::Packet> p, ns3::Ipv4Address const & source, ns3::Ipv4Address const & destination, ns3::Ptr<ns3::Ipv4Interface> interface) [member function]
    cls.add_method('Receive', 
                   'ns3::Ipv4L4Protocol::RxStatus', 
                   [param('ns3::Ptr< ns3::Packet >', 'p'), param('ns3::Ipv4Address const &', 'source'), param('ns3::Ipv4Address const &', 'destination'), param('ns3::Ptr< ns3::Ipv4Interface >', 'interface')], 
                   is_virtual=True)
    ## udp-l4-protocol.h: void ns3::UdpL4Protocol::ReceiveIcmp(ns3::Ipv4Address icmpSource, uint8_t icmpTtl, uint8_t icmpType, uint8_t icmpCode, uint32_t icmpInfo, ns3::Ipv4Address payloadSource, ns3::Ipv4Address payloadDestination, uint8_t const * payload) [member function]
    cls.add_method('ReceiveIcmp', 
                   'void', 
                   [param('ns3::Ipv4Address', 'icmpSource'), param('uint8_t', 'icmpTtl'), param('uint8_t', 'icmpType'), param('uint8_t', 'icmpCode'), param('uint32_t', 'icmpInfo'), param('ns3::Ipv4Address', 'payloadSource'), param('ns3::Ipv4Address', 'payloadDestination'), param('uint8_t const *', 'payload')], 
                   is_virtual=True)
    ## udp-l4-protocol.h: void ns3::UdpL4Protocol::Send(ns3::Ptr<ns3::Packet> packet, ns3::Ipv4Address saddr, ns3::Ipv4Address daddr, uint16_t sport, uint16_t dport) [member function]
    cls.add_method('Send', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Ipv4Address', 'saddr'), param('ns3::Ipv4Address', 'daddr'), param('uint16_t', 'sport'), param('uint16_t', 'dport')])
    ## udp-l4-protocol.h: void ns3::UdpL4Protocol::Send(ns3::Ptr<ns3::Packet> packet, ns3::Ipv4Address saddr, ns3::Ipv4Address daddr, uint16_t sport, uint16_t dport, ns3::Ptr<ns3::Ipv4Route> route) [member function]
    cls.add_method('Send', 
                   'void', 
                   [param('ns3::Ptr< ns3::Packet >', 'packet'), param('ns3::Ipv4Address', 'saddr'), param('ns3::Ipv4Address', 'daddr'), param('uint16_t', 'sport'), param('uint16_t', 'dport'), param('ns3::Ptr< ns3::Ipv4Route >', 'route')])
    ## udp-l4-protocol.h: void ns3::UdpL4Protocol::SetNode(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('SetNode', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')])
    ## udp-l4-protocol.h: ns3::UdpL4Protocol::PROT_NUMBER [variable]
    cls.add_static_attribute('PROT_NUMBER', 'uint8_t const', is_const=True)
    ## udp-l4-protocol.h: void ns3::UdpL4Protocol::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## udp-l4-protocol.h: void ns3::UdpL4Protocol::NotifyNewAggregate() [member function]
    cls.add_method('NotifyNewAggregate', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    return

def register_Ns3Icmpv4L4Protocol_methods(root_module, cls):
    ## icmpv4-l4-protocol.h: ns3::Icmpv4L4Protocol::Icmpv4L4Protocol(ns3::Icmpv4L4Protocol const & arg0) [copy constructor]
    cls.add_constructor([param('ns3::Icmpv4L4Protocol const &', 'arg0')])
    ## icmpv4-l4-protocol.h: ns3::Icmpv4L4Protocol::Icmpv4L4Protocol() [constructor]
    cls.add_constructor([])
    ## icmpv4-l4-protocol.h: int ns3::Icmpv4L4Protocol::GetProtocolNumber() const [member function]
    cls.add_method('GetProtocolNumber', 
                   'int', 
                   [], 
                   is_const=True, is_virtual=True)
    ## icmpv4-l4-protocol.h: static uint16_t ns3::Icmpv4L4Protocol::GetStaticProtocolNumber() [member function]
    cls.add_method('GetStaticProtocolNumber', 
                   'uint16_t', 
                   [], 
                   is_static=True)
    ## icmpv4-l4-protocol.h: static ns3::TypeId ns3::Icmpv4L4Protocol::GetTypeId() [member function]
    cls.add_method('GetTypeId', 
                   'ns3::TypeId', 
                   [], 
                   is_static=True)
    ## icmpv4-l4-protocol.h: ns3::Ipv4L4Protocol::RxStatus ns3::Icmpv4L4Protocol::Receive(ns3::Ptr<ns3::Packet> p, ns3::Ipv4Address const & source, ns3::Ipv4Address const & destination, ns3::Ptr<ns3::Ipv4Interface> incomingInterface) [member function]
    cls.add_method('Receive', 
                   'ns3::Ipv4L4Protocol::RxStatus', 
                   [param('ns3::Ptr< ns3::Packet >', 'p'), param('ns3::Ipv4Address const &', 'source'), param('ns3::Ipv4Address const &', 'destination'), param('ns3::Ptr< ns3::Ipv4Interface >', 'incomingInterface')], 
                   is_virtual=True)
    ## icmpv4-l4-protocol.h: void ns3::Icmpv4L4Protocol::SendDestUnreachFragNeeded(ns3::Ipv4Header header, ns3::Ptr<ns3::Packet const> orgData, uint16_t nextHopMtu) [member function]
    cls.add_method('SendDestUnreachFragNeeded', 
                   'void', 
                   [param('ns3::Ipv4Header', 'header'), param('ns3::Ptr< ns3::Packet const >', 'orgData'), param('uint16_t', 'nextHopMtu')])
    ## icmpv4-l4-protocol.h: void ns3::Icmpv4L4Protocol::SendDestUnreachPort(ns3::Ipv4Header header, ns3::Ptr<ns3::Packet const> orgData) [member function]
    cls.add_method('SendDestUnreachPort', 
                   'void', 
                   [param('ns3::Ipv4Header', 'header'), param('ns3::Ptr< ns3::Packet const >', 'orgData')])
    ## icmpv4-l4-protocol.h: void ns3::Icmpv4L4Protocol::SendTimeExceededTtl(ns3::Ipv4Header header, ns3::Ptr<ns3::Packet const> orgData) [member function]
    cls.add_method('SendTimeExceededTtl', 
                   'void', 
                   [param('ns3::Ipv4Header', 'header'), param('ns3::Ptr< ns3::Packet const >', 'orgData')])
    ## icmpv4-l4-protocol.h: void ns3::Icmpv4L4Protocol::SetNode(ns3::Ptr<ns3::Node> node) [member function]
    cls.add_method('SetNode', 
                   'void', 
                   [param('ns3::Ptr< ns3::Node >', 'node')])
    ## icmpv4-l4-protocol.h: ns3::Icmpv4L4Protocol::PROT_NUMBER [variable]
    cls.add_static_attribute('PROT_NUMBER', 'uint8_t const', is_const=True)
    ## icmpv4-l4-protocol.h: void ns3::Icmpv4L4Protocol::NotifyNewAggregate() [member function]
    cls.add_method('NotifyNewAggregate', 
                   'void', 
                   [], 
                   visibility='protected', is_virtual=True)
    ## icmpv4-l4-protocol.h: void ns3::Icmpv4L4Protocol::DoDispose() [member function]
    cls.add_method('DoDispose', 
                   'void', 
                   [], 
                   visibility='private', is_virtual=True)
    return

def register_functions(root_module):
    module = root_module
    register_functions_ns3_Config(module.get_submodule('Config'), root_module)
    register_functions_ns3_TimeStepPrecision(module.get_submodule('TimeStepPrecision'), root_module)
    register_functions_ns3_addressUtils(module.get_submodule('addressUtils'), root_module)
    register_functions_ns3_internal(module.get_submodule('internal'), root_module)
    register_functions_ns3_olsr(module.get_submodule('olsr'), root_module)
    return

def register_functions_ns3_Config(module, root_module):
    return

def register_functions_ns3_TimeStepPrecision(module, root_module):
    return

def register_functions_ns3_addressUtils(module, root_module):
    return

def register_functions_ns3_internal(module, root_module):
    return

def register_functions_ns3_olsr(module, root_module):
    return

